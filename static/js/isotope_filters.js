


 
    $(function () {
  var qsRegex;
  var buttonFilter;
  var $container = $('.isotope').isotope({
      itemSelector: '.element-item',
      layoutMode: 'fitRows',
      filter: function () {
          var $this = $(this);
          var searchResult = qsRegex ? $this.text().match(qsRegex) : true;
          var buttonResult = buttonFilter ? $this.is(buttonFilter) : true;
          return searchResult && buttonResult;
      }
  });
  $('#filters').on('click', 'button', function () {
      buttonFilter = $(this).attr('data-filter');
      $container.isotope();
  });
  var $quicksearch = $('#quicksearch').keyup(debounce(function () {
      qsRegex = new RegExp($quicksearch.val(), 'gi');
      $container.isotope();
  }));
  $('.button-group').each(function (i, buttonGroup) {
      var $buttonGroup = $(buttonGroup);
      $buttonGroup.on('click', 'button', function () {
          $buttonGroup.find('.is-checked').removeClass('is-checked');
          $(this).addClass('is-checked');
      });
  });
});
function debounce(fn, threshold) {
  var timeout;
  return function debounced() {
      if (timeout) {
          clearTimeout(timeout);
      }
      function delayed() {
          fn();
          timeout = null;
      }
      setTimeout(delayed, threshold || 100);
  };
}
    //@ sourceURL=pen.js
