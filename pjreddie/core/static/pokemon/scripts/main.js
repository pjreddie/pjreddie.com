/**
 * @jsx React.DOM
 */

var PlayerSection = React.createClass({
  render: function() {
    if (this.props.poke.isDead()) {
      return (
         <div>
          <img class="cocktail" src="table.png"></img>
         <img src='bigheart.png' class='heart-icon' style={{width: '60px', height: '60px'}}/>
         <div class={"poke died topPoke pokemon-"+this.props.poke.id_number}></div>
          <BottomBar pokes={this.props.pokes} poke={this.props.poke}/>
          <Menu pokes={this.props.pokes} poke={this.props.poke}/>
         </div>
         )
      }
    else {
      return (
        <div>
          <img class="cocktail" src="table.png"></img>
          <div class={"poke bottomPoke pokemon-"+this.props.poke.id_number}></div>
          <BottomBar pokes={this.props.pokes} poke={this.props.poke}/>
          <Menu pokes={this.props.pokes} poke={this.props.poke}/>
        </div>
      )
    }
  }
})

var EnemySection = React.createClass({
  render: function() {
      if (this.props.poke.isDead()) {
        return (
           <div>
         <img src='bigheart.png' class='heart-icon op' style={{width: '60px', height: '60px'}}/>
         <div class={"poke died op topPoke pokemon-"+this.props.poke.id_number}></div>
           <TopBar pokes={this.props.pokes} poke={this.props.poke}/>
           </div>
           )
        }
      else {
        return (
         <div>
         <div class={"poke topPoke pokemon-"+this.props.poke.id_number}></div>
         <TopBar pokes={this.props.pokes} poke={this.props.poke}/>
         </div>
        )
      }
  }
})

var App = React.createClass({
  getInitialState: function() {
    return {
    }
  },
  handleChange: function(event) {
    console.log('here')
  },

  render: function() {

    playerPokes = []
    $.each(this.props.game.playerPokemon, function(i,e){
      if (!e.isDead())
        playerPokes.push(e)
    })
    badPokes = []
    $.each(this.props.game.computerPokemon, function(i,e){
      if (!e.isDead())
        badPokes.push(e)
    })
    playerPokemon = this.props.game.currPlayerPokemon,
    badPokemon =  this.props.game.currComputerPokemon
    if (playerPokes.length == 0) {
      return (
        <div class='lose'>
          <span class='title'>Mr right is out there somewhere, but he's not here</span>
        </div>
      )
    } else if (badPokes.length == 0) {
      return (
        <div class='win'>
          <span class='title'> Your Love is unmatched </span>
        </div>
      )
    } else if(window.scared) {
      return (
        <div class='lose'>
          <span class='title'> Dont be afraid to open up</span>
        </div>
        )
    }else {
      return (
        <div>
          <div class=''>
            <div class=''>
              <EnemySection pokes={badPokes} poke={badPokemon} />
            </div>
            <div class=''>
              <PlayerSection pokes={playerPokes} poke={playerPokemon} />
            </div>
          </div>
        </div>
      )
    }
  }
})

setTimeout(function(){
  setInterval(function() {
    React.renderComponent(
      <App game={Game}/>,
      document.getElementById('stuff')
    );
  }, 100);
}, 2000)
