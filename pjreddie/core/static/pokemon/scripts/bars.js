/**
 * @jsx React.DOM
 */

var PokeList = React.createClass({
  render: function() {
    var createEgg = function(poke) {
      return ( <span> * </span> )
    }
    return (
      <div class="pokeList">
        { this.props.pokes.map(createEgg) }
      </div>
    )
  }
})

var MonsterInfo = React.createClass({
  render: function() {
    return (
      <div>
        <span class="name">{ this.props.name }</span>
      </div>
    )
  }
})

var HealthBar = React.createClass({
  render: function() {
    hpPercent = (this.props.curr / this.props.max) * 100
    return (
      <div class="progress progress-striped">
        <div class="progress-bar progress-bar-danger" role="progressbar" style={{width: hpPercent+'%'}}>
          <span class="sr-only">80% Complete (danger)</span>
        </div>
      </div>
    )
  }
})

var TopBar = React.createClass({
  render: function() {
    var createItem = function(itemText) {
      return <MenuItem name={itemText} />
    }
    return (
      <div class='info topInfo'>
          <MonsterInfo name={this.props.poke.name} />
          <div class='backbar'>
            <img class='heart' src='heart.png' />
        <div class='bar topBar'>
          <HealthBar max={this.props.poke.maxHP} curr={this.props.poke.currHP}/>
        </div>
        </div>
      </div>
    );
  }
});

var BottomBar = React.createClass({
  render: function() {
    var createItem = function(itemText) {
      return <MenuItem name={itemText} />
    }
    return (
     <div class='info bottomInfo'>
        <PokeList pokes={this.props.pokes} />
        <MonsterInfo name={this.props.poke.name}/>
          <div class='backbar'>
            <img class='heart' src='heart.png' />
        <div class='bar bottomBar'>
          <HealthBar max={this.props.poke.maxHP} curr={this.props.poke.currHP}/>
        </div>
        </div>
      </div>
    );
  }
})
