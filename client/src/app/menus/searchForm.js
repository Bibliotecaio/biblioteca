angular.module('searchForm', [
	'ui.router'
])
  
.directive('searchForm',
  function searchForm($state, $stateParams) {
    return {
      restrict: 'E',
      replace: true,
      scope: false,
      template: `
        <div>
          <form class="input-group document-ui-search-books col-md-10" ng-submit="vm.submitQueries(vm.page, vm.search.queries)">
            <input type="search"
                   class="form-control input-sm"
                   placeholder="например: часослов, постановления соборов, синодик"
                   clear-btn reload="vm.submitQueries()"
                   ng-model="vm.search.queries">
              <span class="input-group-btn">
                <input type="submit" value="" class="search-button"/>
              </span>
          </form>
          <div class="search-info">
            {{vm.results.count | russian_pluralize: ['Найден', 'Найдены', 'Найдено']}}
            {{vm.results.count}}
            {{vm.results.count | russian_pluralize: ['результат', 'результата', 'результатов']}}
          </div>
        </div>
        `,
      link: function ($scope, elem, attrs) {
      }
    };
});
