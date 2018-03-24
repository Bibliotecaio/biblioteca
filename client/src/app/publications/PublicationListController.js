angular.module('PublicationListController', [
  'ui.router'
])

.controller('PublicationListController',
  function PublicationListController($state, $stateParams, dataService) {
    let vm = this;

    const page = parseInt($stateParams.page, 10) || 1;
    vm.state = $state.$current.name;
    
    let getDocuments = function (searchObject) {
      dataService.publications.get(searchObject).$promise.then(function(response) {
        // success
        vm.results = response;
      }, function(errResponse) {});
    };
    
    // Init
    getDocuments({page: page});
});
