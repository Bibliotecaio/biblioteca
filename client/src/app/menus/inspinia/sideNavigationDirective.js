angular.module('sideNavigationDirective', [
])
  
/**
 * sideNavigation - Directive for run metsiMenu on sidebar navigation
 */
.directive('sideNavigationDirective',
  function sideNavigationDirective($timeout) {
    return {
      restrict: 'A',
      link: function(scope, element) {
        // Call the metsiMenu plugin and plug it to sidebar navigation
        $timeout(function(){
          element.metisMenu();
        });
      }
    };
});