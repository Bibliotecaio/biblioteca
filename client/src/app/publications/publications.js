angular.module('documentUI.publications', [
  'PublicationListController',
  'PublicationDetailController',
  'ui.router'
])

.config(function config($stateProvider) {
  $stateProvider
    .state('publications', {
      abstract: true,
      url: '/publications',
    })
    
    .state('publications.all', {
      parent: 'publications',
      url: '/?page',
      views: {
        'navigation@': {},
        'topnavbar@': {
          templateUrl: 'views/header.tpl.html',
        },
        'main@': {
          templateUrl: 'publications/publication_list.tpl.html',
          controller: 'PublicationListController as vm',
        },
        'footer@': {
          templateUrl: 'views/footer-min.tpl.html',
        },
        
      },
      params: {
        page: {
            value: '0',
            squash: true
        }
      },
      data: {
        title: 'Публикации',
        access: ['editor', 'admin', 'anonymous'],
        specialClass: 'main-bg',
        wrapperClass: 'no-margin-no-padding',
        containerClass: 'container document-ui-container'
      }
    })
    .state('publications.detail', {
      parent: 'publications',
      url: '/:id',
      views: {
        'navigation@': {},
        'topnavbar@': {
          templateUrl: 'views/header.tpl.html',
        },
        'main@': {
          templateUrl: 'publications/publication_detail.tpl.html',
          controller: 'PublicationDetailController as vm',
        },
        
        'footer@': {
          templateUrl: 'views/footer-min.tpl.html',
        },
        
      },
      data: {
        access: ['editor', 'admin', 'anonymous'],
        specialClass: 'main-bg',
        wrapperClass: 'no-margin-no-padding',
        containerClass: 'container document-ui-container'
      }
    })
});