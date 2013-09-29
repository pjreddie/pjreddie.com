var Game = function() {
   var that = {};

   var movesLoaded = false;

   // crude onReady
   that.readyQueue = [];
   that.onReady = function(f) {
      that.readyQueue.push(f);
   }

   that.moves = {};
   that.pokemon = {};
   that.currPlayerPokemon = {};
   that.currComputerPokemon = {};
   that.playerPokemon = [];
   that.computerPokemon = [];

   // turn stuff
   that.isComputersTurn = false;
   that.currProt = {};
   that.currOpp = {};
   that.playerQueue = [];
   that.computerQueue = [];

   that.onPlayer = function(f) {
      that.playerQueue.push(f);
   }
   
   that.onComputer = function(f) {
      that.computerQueue.push(f);
   }

   that.runPlayer = function() {
      for (idx in that.playerQueue) {
         that.playerQueue[idx]();
      }
   }

   that.runComputer = function() {
      for (idx in that.computerQueue) {
         that.computerQueue[idx]();
      }
   }

   that.switchTurn = function() {
      that.isComputersTurn = !that.isComputersTurn;
      if(that.isComputersTurn) {
        that.currProt = that.currComputerPokemon;
        that.currOpp = that.currPlayerPokemon;
      }
      else {
        that.currProt = that.currPlayerPokemon;
        that.currOpp = that.currComputerPokemon;
      }
      if (that.isComputersTurn) { that.runComputer(); }
      else { that.runPlayer(); }
   }

   that.applyStatusEffects = function() {
      console.log("applying status effects");

      var currPoke = that.currProt;
      var keepList = [];
      while(currPoke.statusEffects.length > 0)
      {
         var effect = currPoke.statusEffects.shift();
         switch(effect) {
            case 1: // sleep
               console.log("attempting sleep");
               if (Math.random() > 0.6) {
                  console.log("doing sleep");
                  Game.switchTurn();
               }
               if (Math.random() > 0.6) {
                  console.log("removing Effect");
                  keepList.push(effect);
               }
               break;
            case 4: // poison
               console.log("attempting poison damage");
               if (Math.random() > 0.6) {
                  console.log("doing poison damage "+ Math.max(currPoke.maxHP / 16,1));
                  currPoke.damage(Math.max(currPoke.maxHP / 16,1));
               }
               if (Math.random() > 0.6) {
                  console.log("removing Effect");
                  keepList.push(effect);
               }
               break;
         }
      }
      currPoke.statusEffects = keepList;
   }

   that.genMonster = function (id_number, owner) {
      if (id_number < 1 || id_number > 151)
      {
         mon = Monster({
            "name"         : "MissingNo",
            "hp"        : 9999,
            "atk"          : 9999,
            "def"          : 9999,
            "speed"        : 9999,
            "evolveTo"     : -1,
            "evolveLevel"  : -1
         });
      } else {
         var mon = Monster(that.pokemon[id_number]);
      }
      mon.owner = owner
      return mon
   }

  that.compPickNewPoke = function() {
    var poke; 
    $.each(that.computerPokemon, function(i,e) {
      if (!poke && !e.isDead()) {
        poke = e
      }
    })

    if (poke)
      that.currComputerPokemon = poke
    else
      console.log('you win')
  }

   // Load data
   $.getJSON( "moves.json", function(data) {
      $.each(data, function(key, val) {
         that.moves[key] = {
            "name"   : val.name,
            "pp"     : val.pp
         };

         // build the attack function
         that.moves[key].func = function (poke1, poke2) {
            var result = {};
            speak(poke1['name'] + ' uses ' + val.name, {amplitude: 800})
            console.log("Attacking");
            console.log(val);

            if (val.moveType === "simple") { // just attempt attack
               result.hitsOpponent = true;

               var isSTAB = (val.type == poke1.type);
               var STAB = isSTAB ? 1.5 : 1;
               var randomNumber = (Math.random()*15)+85;
               var totalDMG = ((((2 * poke1.level / 5 + 2) * poke1.atk * val.power / poke2.def) / 50) + 2) * STAB /** Weakness/Resistance*/ * randomNumber / 100;
               console.log("damage " + totalDMG);
               if (Math.random() < val.accuracy) {
                  poke2.damage(totalDMG);
                  result.hitAmount = totalDMG;
                  result.missed = false
               } else {
                  result.missed = true;
               }
            } else if (val.moveType === "applyStatus") {
               result.applyStatus = true;
               if (Math.random() < val.accuracy) {
                  poke2.statusEffects.push(val.applyStatus);
                  result.missed = false;
               } else {
                  result.missed = true;
               }
            }

            console.log(result);
            that.switchTurn();
            return result;
         }
      });
      movesLoaded = true;
   });

   $.getJSON( "pokemon.json", function(data) {
      while (!movesLoaded) {}
      $.each(data, function(key, val) {
         that.pokemon[key] = {
         "name"         : val.name,
         "id_number"    : key,
         "type"         : val.type1,
         "hp"           : val.baseStats.hp,
         "atk"          : val.baseStats.atk,
         "def"          : val.baseStats.def,
         "spAtk"        : val.baseStats.spAtk,
         "spDef"        : val.baseStats.spDef,
         "speed"        : val.baseStats.speed,
         "evolveTo"     : val.evolveTo,
         "evolveLevel"  : val.evolveLevel,
         "attacks"      : [],
         "owner"        : null
         };

        for (l in val.learnset) {
           that.pokemon[key].attacks.push(val.learnset[l].move);
        }

      });

      while (that.readyQueue.length > 0) {
             (that.readyQueue.shift())();   
      }
   });

   return that;
}();

var Monster = function(spec) {
   var that = {};

   that.name = spec.name;
   that.id_number = spec.id_number;
   that.type = spec.type;
   that.maxHP = spec.hp;
   that.currHP = spec.hp;
   that.atk = spec.atk;
   that.def = spec.def;
   that.spAtk = spec.spAtk;
   that.spDef = spec.spDef;
   that.speed = spec.speed;
   that.level = 10;
   that.attackData = {};
   that.attacks = {};
   that.statusEffects = [];

   // add attacks
   for (idx in spec.attacks)
   {
      if (Object.keys(that.attacks).length > 3) { continue; }
      var attack_name = spec.attacks[idx];
      var attack_data = Game.moves[attack_name];
      if (typeof attack_data != "undefined") {
         console.log("attack_name: " + attack_name);

         (function (attack_name, attack_data) {

            that.attackData[attack_name] = {
               "name"         : attack_data.name,
               "maxPP"        : attack_data.pp,
               "currPP"       : attack_data.pp,
               "attackFunc"   : attack_data.func
            };

            that.attacks[attack_name] = function() {
               var my_attackData = that.attackData[attack_name];
               if (my_attackData.currPP > 0)
               {
                  my_attackData.currPP -= 1;
                  return attack_data.func(Game.currProt, Game.currOpp);
               } else {
                  console.log("Can't use attack" + attack_name);
                  return {};
               }
            }
         })(attack_name, attack_data);
      }
   }

   that.levelUp = function() { that.level += 1; }

   that.damage = function(dmg) {
      that.currHP = that.currHP - dmg;
      if (that.currHP < 0) {
         console.log("Underflowed HP!");
         that.currHP = 0;
         that.die()
      }
   };

   that.isDead = function() {
      return that.currHP <= 0;
   }

   that.die = function() {
     setTimeout(function() {
       if (that.owner == 'computer') {
         console.log(that.owner)
         Game.compPickNewPoke()
       }
     }, 1000)
   }
   
   that.heal = function(hlth) {
      that.currHP = that.currHP + hlth;
      if (that.currHP > that.maxHP) { 
         console.log("Overflowed HP!");
         that.currHP = that.maxHP;
      }
   };

   that.isDead = function() {
      return that.currHP <= 0;
   };

   that.tryEvolve = function() {
      if (that.level >= spec.evolveLevel) {
         return Game.genMonster(spec.evolveTo);
      }
      return that;
   }

   return that;
}
Game.onPlayer( Game.applyStatusEffects );
Game.onComputer( Game.applyStatusEffects );


Game.onComputer( function() {
   var poke = Game.currComputerPokemon;
   console.log(Game.currProt);
   setTimeout(function(){
     for (key in poke.attacks) {
        if (Math.random() > 0.5) {
           poke.attacks[key](); break;
        }
     }
   }, 3000)
   //Game.switchTurn();
});

Game.onReady( function() { 
   var ids = [];
   for (var i = 0; i < 6; i++) {
      ids[i] = Math.round((Math.random()*149)+1);
   }
   var bulba = Game.genMonster(ids[0], 'player');
   var charm = Game.genMonster(ids[1], 'player');
   var squir = Game.genMonster(ids[2], 'player');
   var tmp = Game.playerPokemon;
   tmp.push(bulba);
   tmp.push(charm);
   Game.currPlayerPokemon = Game.playerPokemon[0];
   Game.currProt = Game.currPlayerPokemon;

   var bulba = Game.genMonster(ids[3], 'computer');
   var charm = Game.genMonster(ids[4], 'computer');
   var squir = Game.genMonster(ids[5], 'computer');

   var tmp = Game.computerPokemon;
   tmp.push(bulba);
   tmp.push(charm);

   Game.currComputerPokemon = Game.computerPokemon[0];
   Game.currOpp = Game.currComputerPokemon;
});
