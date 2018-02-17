//OnlineAddressBook = OAB
var OAB = OAB || {};
$(function(){

	if(!OAB.dashboard){
        OAB.dashboard = {}
    }

    var getQPathParams = function(index, pathname) {
        if(!pathname){
            pathname = window.location.pathname;
        }
        var pathArray = pathname.split( '/' );
        return pathArray[index];
    };

    var UMAP = {
        "group" : "/api/groups",
    	"person" : "/api/persons",
        "person_search" : "/api/persons/search",
    };

    var fetchGroups = function() {
    	$.ajax({
              type: "GET",
              cache: false,
              url: UMAP["group"]
        }).done(function(response){
            if(response.data.length > 0){
                var grpListTpl = $( "#grp-list-tpl" );
                if(grpListTpl.length > 0){
                    var template = _.template(grpListTpl.html());
                    $("#grp-list-container").append(template(response ));
                }
            }
        });
    };

    var fetchPerson = function(personId) {
        $.ajax({
              type: "GET",
              cache: false,
              url: UMAP["person"]+"/"+personId
        }).done(function(response){
            if(response.data){
                var tpl = $( "#prs-show-tpl" );
                if(tpl.length > 0){
                    var template = _.template(tpl.html());
                    $("#pshw").append(template(response.data ));
                }
            }
        });
    };

    var fetchGroup = function(groupId) {
        $.ajax({
              type: "GET",
              cache: false,
              url: UMAP["group"]+"/"+groupId
        }).done(function(response){
            if(response.data){
                var tpl = $( "#grp-show-tpl" );
                if(tpl.length > 0){
                    var template = _.template(tpl.html());
                    $("#gshw").append(template(response.data ));
                }
            }
        });
    };

    var addGroup = function(groupName) {
        $.ajax({
            type: "POST",
            cache: false,
            url: UMAP["group"],
            data: JSON.stringify({name:groupName}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
        }).done(function(response){
            if(response.data.id){
                window.location = "/";
            }
        });
    };

    var addPerson = function(data) {
        $.ajax({
            type: "POST",
            cache: false,
            url: UMAP["person"],
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
        }).done(function(response){
            if(response.data.id){
                window.location = "/";
            }
        });
    };

    var searchPerson = function(stext) {
        $.ajax({
            type: "POST",
            cache: false,
            url: UMAP["person_search"],
            data:{text:stext}
        }).done(function(response){
            var template = _.template('User Found: <a href="/persons/<%- id %>"><%- first_name %></a><br> '+
                'Last Name: <%- last_name %>');
            $(".search .found").append(template(response.data ));
        });
    };

    $(".ngrp").click(function(ev){
        addGroup($(".gname").val());
    });
    
    $(".nprs").click(function(ev){
        ev.preventDefault();
        var seri = $('#new-person').serializeObject();
        addPerson(seri);
    });

    $(".search button").click(function(ev){
        $(".search .found").empty();
        searchPerson($(".search input").val());
    });
    
    $(".more").click(function(ev){
        var input = $(this).prev("input");
        if(input.length == 0) {
            input = $(this).prev("select");
        }
        var newInput =input.clone();
        var oldId = $(newInput).attr('id');
        var idList = oldId.split('-');
        var newId = parseInt(idList[1])+1;
        newInput.attr("id", idList[0]+"-"+newId+"-" +idList[2]);
        newInput.attr("name", idList[0]+"-"+newId+"-" +idList[2]);
        ($(this)).before(newInput);
    });


    if(location.pathname === "/"){
        fetchGroups();
    }
    else if(location.pathname.indexOf("/groups/") !== -1){
        var groupId = getQPathParams(2);
        fetchGroup(groupId);
    }
    else if(location.pathname.indexOf("/persons/") !== -1){
        var personId = getQPathParams(2);
        fetchPerson(personId);
    }

    $.fn.serializeObject = function() {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function() {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };
    

});
