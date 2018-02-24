var vm = new Vue({
    el: '#main',
    data:{
        risk: ''
    },
    created: function () {
        this.fetchData();
    },
    methods: {
        fetchData: function() {
            
            const self = this;

            let env = document.querySelector('[name=env]').getAttribute('value');
            env = ((env) ? '/'+env : '');

            $.ajax({
                type: "GET",
                cache: false,
                url: `${env}/api/v1/risks/2`
            }).done(function(response){
                self.risk = response.data;
                console.log(self.risk);
            });
        }
    }
});
