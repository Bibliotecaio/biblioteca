angular.module('searchMinForm', [
	'ui.router'
])
	
  
.directive('searchMinForm',
  function searchMinForm(searchService) {
    return {
      restrict: 'E',
      replace: true,
      scope: {},
      template: `
        <form class="input-group document-ui-nav-search" ng-submit="submitQueries(1, mainSearchForm)">
          <input type="search" 
                 class="form-control input-sm" 
                 placeholder="Поиск" 
                 clear-btn 
                 reload="submitSearchQueries()"
                 ng-model="mainSearchForm">
          <span class="input-group-btn">
            <input type="submit" value="" class="search-button"/>
          </span>
        </form>`,
      link: function (scope, elem, attrs) {
        scope.submitQueries = searchService.submitQueries
      }
    };
});
