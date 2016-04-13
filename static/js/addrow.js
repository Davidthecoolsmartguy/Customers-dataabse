$(window).load(function(){
$(document).ready(function () {

    (function () {

        


        $('form').on('click', '.addRow', function () {
            var start = $('table'),
                newRow = $('<div class="item-row"> <div class="main-row"> <div class="delete"></div> <div class="amount value"> <span class="currency-symbol">$</span>0 </div> <div class="unit_cost"> <div class="input-group"> <span class="input-group-addon currency-sign">$</span> <input class="item-calc form-control" type="number" step="any" autocomplete="off" name="items[0][unit_cost]"> </div> </div> <div class="quantity"> <input type="number" step="any" class="item-calc form-control" autocomplete="off" name="items[0][quantity]"> </div> <div class="name"> <textarea class="item-calc form-control" rows="1" name="items[0][name]" placeholder="Description of item/service..."></textarea> </div> </div> </div>');
            $(start).append(newRow);
        });
        
    })(); //end SIAF

}); //end document.ready
});//]]> 
