angular.module('documentUI.books', [
  'BookListController',
  'BookViewController',
  'ui.router'
])

.config(function config($stateProvider) {
  $stateProvider
    .state('books', {
      abstract: true,
      url: '/documents',
    })
    
    .state('books.all', {
      parent: 'books',
      url: '/:id?page',
      views: {
        'navigation@': {},
        'topnavbar@': {
          templateUrl: 'views/header.tpl.html',
        },
        'main@': {
          templateUrl: 'books/book_list.tpl.html',
          controller: 'BookListController as vm',
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
        title: 'Архив и Библиотека',
        access: ['editor', 'admin', 'anonymous'],
        specialClass: 'main-bg',
        wrapperClass: 'no-margin-no-padding',
        containerClass: 'container document-ui-container'
      }
    })
    .state('books.all.viewer', {
      parent: 'books.all',
      url: '/view',
      views: {
        'navigation@': {},
        'topnavbar@': {},
        'main@': {
          templateUrl: 'books/book_view.tpl.html',
          controller: 'BookViewController as vm',
        },
        'footer@': {},
      },
      data: {
        access: ['editor', 'admin', 'anonymous'],
        containerClass: 'wowbook-container',
      }
    })
});