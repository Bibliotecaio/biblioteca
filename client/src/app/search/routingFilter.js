angular.module('routingFilter', [
])

.filter('routingFilter', function routingFilter() {
  
      function getRoute(result) {
        if (result.section==='publications') {
          return `${result.section}.detail({id: ${result.id}})`
        }
        if (result.section==='books') {
          return `${result.section}.all({id: ${result.id}})`
        }
      }
      return function(result){
        return getRoute(result);
      };
    });

