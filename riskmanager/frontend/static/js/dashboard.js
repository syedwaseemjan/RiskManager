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
            $.ajax({
                type: "GET",
                cache: false,
                url: "/api/v1/risks/2"
            }).done(function(response){
                self.risk = response.data;
                console.log(self.risk);
            });
        }
    }
});
