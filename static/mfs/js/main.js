var nm = new Vue({
  el: '#app',
  data: {
    messages: []
  },
  methods:{
    get_messages: function(){
        fetch('http://deadrigger.pythonanywhere.com/api/first?get_messages='+this.messages[0].pk)
        .then(response => response.json())
        .then(json => this.update(json))
    },
    mark_read: function(id){
        fetch("http://deadrigger.pythonanywhere.com/api/first?mark_read="+id)
    },
    update: function(data){
        for(index = 0, len = data.length; index < len; ++index){ this.messages.splice(0,0,data[index])}
    }
  },
  created(){
    fetch('http://deadrigger.pythonanywhere.com/api/first')
      .then(response => response.json())
      .then(json =>
        this.messages = json)
  }
})
var update = setInterval(nm.get_messages, 10000)