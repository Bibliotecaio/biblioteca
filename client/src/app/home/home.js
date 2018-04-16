angular.module('documentUI.home', [
  'HomeController',
  'documentPlaceFilter'
])

.config(function config($stateProvider) {
  $stateProvider
    .state('home', {
      url: '/',
      views: {
        'navigation@': {},
        'topnavbar@': {
          templateUrl: 'views/header.tpl.html'
        },
        'main@': {
          templateUrl: 'books/book_list.tpl.html',
          controller: 'BookListController as vm',
        },
        'footer@':  {
          templateUrl: 'views/footer-min.tpl.html'
        }
      },
      data: {
        access: ['anonymous', 'editor', 'admin'],
        title: 'Главная',
        specialClass: 'main-bg',
        wrapperClass: 'no-margin-no-padding',
        containerClass: 'container document-ui-container'
      }
    })
});