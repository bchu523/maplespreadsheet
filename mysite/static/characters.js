$(document).ready(function(){
    var add = (function () {
    var counter = 0;
    return function () {return counter += 1;}
    })();
    $(".table").on("click","tr>td>#hide",function(){
        //$("#tooltip").attr('id', 'tooltiph');
        $(this).parent().parent().find(".display").hide();
        $(this).parent().parent().find(".input").show();
        //$(this).parent().parent().find("#tooltip").show();



    });
$( "li.item-ii" ).find( "li" ).css( "background-color", "red" );

    $(document).on("click", "#btn",function(){
        //$(this).parent().parent().find("#tooltip").hide();
        //$("#tooltiph").attr('id', 'tooltip');

        var items  = $(this).parent().parent().find( ".item" )
        console.log(items);
        items.each(function(){

        var item1 = $(this).find(".icon").val();
        console.log(item1);
        $(this).find("#icon").attr("src",item1);
        var item1 = $(this).find(".tooltipd").val();
        console.log(item1);
        $(this).find("#tooltip").attr("src",item1);


        });
        $(this).parent().parent().find(".display").show();
        $(this).parent().parent().find(".input").hide();
        var character = $(this).parent().parent().find('.sprite').val();
        $(this).parent().parent().find("#char").attr("src",character);
        var charactername = $(this).parent().parent().find('.title').val();
        $(this).parent().parent().find("#charname").text(charactername);

        //var item1 = $(this).parent().parent().find('#item1').val();
        //$(this).parent().parent().find(".display>#i1>#i1").attr("src",item1);
        //$(this).parent().parent().find(".display>.tooltip").attr("src",item1);


        $('table').append('<tr><input class="remove" value="remove"></tr>');
    });
    $(".table").on("click","tr>td>.new",function() {
        //var id = ($(".grid3x3 .display .equip").length + 1).toString();
        //console.log(id)
                var id = add();
                console.log(id);
                $(this).parent().parent().find(".equip").append('<div class="item" id = "0"> <img src=""  id="tooltip">  <img src="" id="icon"><div class="input" id="0"> <div class="form-group" id="0"> <label for="item1">Icon:</label> <input type="text" class="form-control icon" id="item1" value="Enter icon url"></div> <div class="form-group" id="0"> <label for="item2">Tooltip:</label> <input type="text" class="form-control tooltipd" id="item2" value="Enter tooltip url"></div>  <a class="remove_block" href="#">Remove</a></div></div></div>');
    //$("#tooltip").attr('id', 'tooltiph');

    //$(this).parent().parent().parent().parent().parent().append('<img src="swrod.jpg"  id="tooltip">');
    $(this).parent().parent().find(".input").show();




    });

$(document).on('click','#icon',function() {
    // hover starts code here
    //$(this).show();
//    console.log('hi');
    $(this).parent().find("#tooltip").show();

});
$(document).on('click',"#tooltip", function() {
     //hover starts code here
    //$(this).show();
    $(this).hide();

});

/*$(".tooltip").on({
    mouseover: function () {
        console.log(this);
       //$(this).parent().parent().find(".tooltip").show();
       $(this).show();
    }
    ,
    mouseleave: function () {
       //$(this).parent().parent().find(".tooltip").hide();
       $(this).hide();
    }}
,"tr>td>.equip>.item>.i1>img#i1");*/




    $(document).on("click", ".remove_block", function(events){
    console.log("hi");
    console.log($(this).parent())
    var id = $(this).parent().find(".icon").attr('id');
    console.log(id);
    var data1 = {"id":id};
    $.ajax({
            data:JSON.stringify(data1),
            type: "POST",
            url: '/deletelink',
            contentType:"application/json",
        });
    $(this).parent().parent().remove();
    });
    $("#show").click(function(){
        $("p").show();
    });

    $('.entry').on('click' ,function(){
        $('.table').append(`

<tr>
        <td>
            <img src=""  id="char">
            <div class="form-group input" id="0">
                <input type="text" class="form-control sprite" id="-1" value="Enter profile picture url">
            </div>

        </td>
        <td>
            <p id = "charname"> Click to Edit to change and View to save </p>
            <div class="form-group input" id="0">
                <input type="text" class="form-control title"  value="Click to Edit to change and View to save" id="-1">
            </div>
        </td>
        <td>
            <div class="equip">
            </div>
        </div>
        <a class="new input"> Add</a>
        </td>
        <td>
            <button id="hide">Edit</button>
            <button id="btn">View</button>
        </td>
      </tr>

            `)
    });

$(document).on('input','.form-control',function () {
    if (!$(this).hasClass("changed"))
    {
        $(this).addClass("changed");
        console.log("notchanged");
    }
});

var removeLink = function(){
    var id = $(this).attr('id');
    console.log(id);
    var data1 = {"id":id};
    $.ajax({
            data:JSON.stringify(data1),
            type: "POST",
            url: '/deletelink',
            contentType:"application/json",
        });
    $(this).parent().parent().remove();

}



var addLink = function(row){
        console.log('click!')
        var tooltip = row.find(".tooltipd").map(function() {
                return $(this);

        }).get();
        //split by id to add or to update
        var title = row.find(".title").map(function() {
                return $(this);
        }).get();

        var sprite = row.find(".sprite").map(function() {
                return $(this);
        }).get();

        var icon = row.find(".icon").map(function() {
                return $(this)


        }).get();


        console.log(title);
        console.log(icon);
        console.log(sprite);
        console.log(tooltip);




        $(this).parent().parent().find(".form-control").removeClass("changed");
        console.log(tooltip.length)
        for (x = 0; x<tooltip[0].length;x++)
        {
        //console.log(tooltip[x])
        //var data1 = {"sprite": {"name":[sprite[0].val(),sprite[1]],"title":[title[0].val(),title[1]]},"equip": {"tooltip": [tooltip[x].val(),tooltip[1]], "icon":[icon[x].val(),icon[1]] }}
        //console.log(tooltip[x].val())

    }
    var foo = new Array(tooltip.length)
    $.each(foo, function (x, item) {
         console.log(x);
         var spritetitle = tooltip[x].parent().parent().parent().parent().parent().parent().find(".title");
         var spritename = tooltip[x].parent().parent().parent().parent().parent().parent().find(".sprite");

         var data1 = {"sprite": {"name":[spritename.val(),spritename.attr('id')],"title":[spritetitle.val(),spritetitle.attr('id')]},"equip": {"tooltip": [tooltip[x].val(),tooltip[x].attr('id')], "icon":[icon[x].val(),icon[x].attr('id')] }}
         console.log(data1)
        $.ajax({
            data:JSON.stringify(data1),
            type: "POST",
            url: '/addlink',
            contentType:"application/json",
            success: function(data){
                console.log(x)
                sprite[0].attr('id', data['sprite']['id'] );
                title[0].attr('id',data['sprite']['id'] );
                tooltip[x].attr('id',data['tooltip']['id'] );
                icon[x].attr('id', data['icon']['id'] );





            }
        });
        });

    }
$(document).on('click', '#btn',  function(){
    addLink($(this).parent().parent());
}

        );
//$(document).on('click', '.remove',  removeLink);
$.ajax({
            type: "GET",
            url: '/readlink',
            contentType:"application/json",
            success: function(data){
                refreshFilenameList(data);
                console.log(JSON.stringify(data))

            }
        });
var refreshFilenameList = function(data){
        var templateText = $("#entry-template").html();
        var template = Handlebars.compile(templateText);
        //data = {"title":"title","body":"body"}
        var renderedText = template(data);
        var renderedDom = $(renderedText);
        $(".table").find("tbody").append(renderedDom);
    };
});
