angular.module('documentPlaceFilter', [
])

.filter('document_place', function documentPlaceFilter() {
  
      function getPlace(place) {
        if (place==='archive') {
          return 'Архив'
        }
        if (place==='library') {
          return 'Библиотека'
        }
      }
      return function(place){
        return getPlace(place);
      };
    });


