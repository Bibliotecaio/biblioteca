angular.module('pageTitleDirective', [
  'pageTitleService'
])
  
.directive('pageTitleDirective',
  function pageTitleDirective($rootScope, $state, pageTitleService) {return {
    link: function(scope, element) {
      
      // Listen
      $rootScope.$on('$stateChangeSuccess',
        function(event, toState, toParams, fromState, fromParams) {
          element.text(pageTitleService._simpleTitle());
        });
      
      // Dynamic title
      pageTitleService.subscribe(scope, function(event, title) {
        element.text(title);
      });
    }
  };
});
