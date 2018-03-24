angular.module('HomeController', [
  'fbPage',
  'ui.router'
])

.controller('HomeController',
  function HomeController($state, $stateParams, dataService, localStorageService) {
    let vm = this;
    
    let getDocuments = function (searchObject) {
      dataService.randomDocuments.get(searchObject).$promise.then(function(response) {
        // success
        vm.randomDocuments = response.results;
        localStorageService.set('randomDocuments', response.results);
      }, function(errResponse) {});
    };
    
    let getPublications = function () {
      dataService.publications.get().$promise.then(function(response) {
        // success
        vm.publications = response.results;
      }, function(errResponse) {});
    };
    
    // Initial
    getDocuments({physicalPlace: 'library archive', limit: 5});
    getPublications();
    
    vm.physicalPlace = {
      place: 'library'
    };
    
    vm.reloadRandom = function (place) {
      getDocuments({physicalPlace: place, limit: 5});
      vm.physicalPlace.place = place;
    };
    
    vm.getRandom = function (place) {
      let documents = localStorageService.get('randomDocuments');
      vm.physicalPlace.place = place;
      
      let randomDocuments = {
        'library': documents.filter((item) => item.physicalPlace === 'library'),
        'archive': documents.filter((item) => item.physicalPlace === 'archive'),
        'library archive': documents,
      };
      vm.randomDocuments = randomDocuments[place];
    };
    
});
