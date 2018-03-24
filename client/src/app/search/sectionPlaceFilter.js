angular.module('sectionPlaceFilter', [
])

.filter('sectionPlace', function sectionPlaceFilter() {
  
      function getSection(section) {
        if (section==='publications') {
          return 'Публикации'
        }
        if (section==='books') {
          return 'Архив и Библиотека'
        }
      }
      return function(section){
        return getSection(section);
      };
    });


