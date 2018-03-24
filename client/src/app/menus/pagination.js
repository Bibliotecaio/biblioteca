angular.module('pagination', [
])
  
.directive('pagination',
  function pagination () {
    return {
      restrict: 'E',
      replace: true,
      template:
        `<div class="btn-group">
          <button class="btn btn-white"
                  ui-sref="{{vm.state}}({page: vm.results.current - 1})"
                  type="button" ng-disabled="!vm.results.previous">
            <i class="fa fa-chevron-left"></i>
          </button>  
          <div class="btn-group" ng-repeat="pageNumber in [] | range: vm.results.totalPages:1">
            <button class="btn btn-white"
                    ui-sref="{{vm.state}}({page: pageNumber})"
                    ng-class="{active: pageNumber == vm.results.current}">{{pageNumber}}</button>
          </div>
          <button class="btn btn-white"
                  ui-sref="{{vm.state}}({page: vm.results.current + 1})"
                  type="button" ng-disabled="!vm.results.next">
            <i class="fa fa-chevron-right"></i>
          </button>
        </div>`
    };
});
