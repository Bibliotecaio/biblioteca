angular.module('BookListController', [
  'sticky',
  'ngTextTruncate',
  'ui.select',
  'ui.router'
])

.controller('BookListController',
  function BookListController($state, $stateParams, $location, dataService, localStorageService, linkToAnchorService) {
    let vm = this;
    
    vm.state = $state.$current.name;
    let page = parseInt($stateParams.page, 10) || 1;
    let documentId = parseInt($stateParams.id, 10) || 0;
    
    let setDefaultLocation = function () {
      // TODO: change location, save filters
      //$location.path('/documents/');
    };
    
    let getDocuments = function (searchObject) {
      dataService.documents.get(searchObject).$promise.then(function(response) {
        // success
        vm.results = response;
      }, function(errResponse) {});
    };
    
    let getInitialFilters = function () {
      dataService.initialFilter.get().$promise.then(function(response) {
        // success
        vm.authors = response.authors;
        vm.keywords = response.keywords;
        vm.languages = response.languages;
        vm.timePeriods = response.timePeriods;
        vm.documentTypes = response.documentTypes;
        vm.subjects = response.subjects;
        vm.alphabetChars = response.alphabetChars;
        
      }, function(errResponse) {});
    };
    
    // Init
    let searchObject = {page: page};
    if (documentId > 0) {
      searchObject['documentId'] = documentId;
    }
    getDocuments(searchObject);
    getInitialFilters();
    
    vm.selectedFilters = {
      authors: [],
      timePeriods: [],
      keywords: [],
      languages: [],
      documentTypes: [],
      subjects: [],
      alphabetChars: []
    };
    
    vm.disabled = undefined;
    vm.physicalPlace = {
      place: 'library archive'
    };
    
    vm.clearFilters = function() {
      vm.physicalPlace.place = 'library archive';
      vm.selectedFilters = {
        authors: [],
        timePeriods: [],
        keywords: [],
        languages: [],
        documentTypes: [],
        subjects: [],
        alphabetChars: []
      };
      getDocuments({page: page});
      setDefaultLocation();
    };
    
    
    vm.filterBooks = function () {
      getDocuments({
        page: page,
        physicalPlace: vm.physicalPlace.place,
        authors: vm.selectedFilters.authors.map((item) => `${item.id}`).join(' '),
        timePeriods: vm.selectedFilters.timePeriods.map((item) => `${item.id}`).join(' '),
        documentTypes: vm.selectedFilters.documentTypes.map((item) => `${item.id}`).join(' '),
        languages: vm.selectedFilters.languages.map((item) => `${item.id}`).join(' '),
        keywords: vm.selectedFilters.keywords.map((item) => `${item.id}`).join(' '),
        subjects: vm.selectedFilters.subjects.map((item) => `${item.id}`).join(' '),
        alphabetChars: vm.selectedFilters.alphabetChars.map((item) => `${item.char}`).join(' '),
      });
      setDefaultLocation();
      linkToAnchorService.toLink('top-search');
    };
    
    vm.search = {};
    
    vm.filterByParam = function (filterName, filterObject) {
      vm.selectedFilters = {
        authors: [],
        timePeriods: [],
        keywords: [],
        languages: [],
        documentTypes: [],
        subjects: [],
        alphabetChars: []
      };
      
      vm.selectedFilters[filterName] = [filterObject];
      let selectedParams = {
        page: page,
        physicalPlace: 'library archive',
      };
      selectedParams[filterName] = vm.selectedFilters[filterName].map((item) => `${item.id}`).join(' ');
      getDocuments(selectedParams);
      setDefaultLocation();
      linkToAnchorService.toLink('top-search');
    };
    
    vm.submitQueries = function () {
      setDefaultLocation();
      getDocuments({page: page, q:vm.search.queries});
      linkToAnchorService.toLink('top-search');
    };
    
});
