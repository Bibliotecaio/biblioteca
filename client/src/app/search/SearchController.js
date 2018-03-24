angular.module('SearchController', [
  'ui.router'
])

.controller('SearchController',
  function SearchController(
    $location, $state, $stateParams, linkToAnchorService, pageTitleService, dataService, searchService) {
    let vm = this;

    const page = parseInt($stateParams.page, 10) || 1;
    vm.page = page;
    const query = $stateParams.q || 'Книги';
    vm.state = $state.$current.name;
    
    let getData = function (searchObject) {
      dataService.search.get(searchObject).$promise.then(function(response) {
        // success
        vm.results = response;
        pageTitleService.publish(`Поиск: ${response.query}`);
      }, function(errResponse) {});
    };
    
    // Init
    getData({page: page, q: query});
    vm.submitQueries = searchService.submitQueries;

});
