angular.module('documentUI.search', [
  'SearchController',
  'sectionPlaceFilter',
  'routingFilter',
  'searchService',
  'ui.router'
])

.config(function config($stateProvider) {
  $stateProvider
    .state('search', {
      abstract: true,
      url: '/search',
    })
    
    .state('search.all', {
      parent: 'search',
      url: '/?page&q',
      views: {
        'navigation@': {},
        'topnavbar@': {
          templateUrl: 'views/header.tpl.html',
        },
        'main@': {
          templateUrl: 'search/results_list.tpl.html',
          controller: 'SearchController as vm',
        },
        'footer@': {
          templateUrl: 'views/footer-min.tpl.html',
        },
        
      },
      params: {
        page: {
            value: '0',
            squash: true
        },
        q: {
            value: '',
            squash: true
        },
        
      },
      data: {
        title: 'Поиск',
        access: ['editor', 'admin', 'anonymous'],
        specialClass: 'main-bg',
        wrapperClass: 'no-margin-no-padding',
        containerClass: 'container document-ui-container'
      }
    })
});