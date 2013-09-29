/**
 * @jsx React.DOM
 */


var MenuItem = React.createClass({
  isFunction: function(x){
    return Object.prototype.toString.call(x) == '[object Function]';
  },

  click: function(event) {
    var thing = menuItems[this.props.name]

    if (!this.isFunction(thing)) {
      menuItems = thing
    } else {
      thing()
      menuItems = topMenuItems()
    }
  },
  render: function() {
    return (
      <div class='menuItem pull-left text-center' style= {{width: '50%'}} onClick={this.click}>
        {this.props.name}
      </div>
    )
  }
})


var topMenuItems = function(){
  poke = Game.currPlayerPokemon
  pswitch = {}

  $.each(Game.playerPokemon, function(i,e) {
    if (e != poke && !e.isDead())
      pswitch[e.name] = function(){
        Game.currPlayerPokemon = e
        Game.switchTurn()
      }
  });

  var menu = {
    'Talk': poke.attacks,
    'Items': {
        'potion': function() {
          Game.playerPokemon[0].heal(10)
          Game.switchTurn()
        }
    },
    'Poke': pswitch,
    'Run!': {
      'Really?!!': function() {
        window.scared = true
      }
    }
  }

  if (Game.currPlayerPokemon.isDead())
    return menu['Poke']
  else
    return menu
}


var Menu = React.createClass({
  getInitialState: function() {
  },
  handleChange: function(event) {
  },
  back: function(event) {
    console.log('heeloo')
    menuItems = topMenuItems()
  },
  render: function() {
    var that = this
    var createItem = function(itemText) {
      return <MenuItem name={itemText} pokes={that.props.pokes} poke={that.props.poke} />
    }
    return (
      <div>
        <div class='menu'>
          { Object.keys(menuItems).map(createItem) }
        </div>
      </div>
    );
  }
});
setTimeout(function(){
window.menuItems = topMenuItems()
}, 2000);
