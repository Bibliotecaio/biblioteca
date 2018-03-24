angular.module('documentUI', [
  'templates-app',
  'templates-common',
  'documentUI.utils',
  'documentUI.menus',
  'documentUI.home',
  'documentUI.books',
  'documentUI.publications',
  'documentUI.search',
  'angular-clear-button',
  'LocalStorageModule',
  'config',
  'toaster',
  'icheck',
  'angularMoment',
  'ngSanitize',
  'angular.filter',
  'ui.bootstrap',
  'ui.router',
])

.config(
  function ($urlMatcherFactoryProvider, $urlRouterProvider,
            $httpProvider, $resourceProvider, $locationProvider,
            localStorageServiceProvider) {
    
    //$locationProvider.html5Mode(true);
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $urlMatcherFactoryProvider.strictMode(false);
    $urlRouterProvider.otherwise('/');
    
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.interceptors.push('httpInterceptor');
    
    localStorageServiceProvider.setPrefix('documentUI');

    
  })

.run(
  function (
    $rootScope, $location, $state, $stateParams, moment, amMoment) {
    amMoment.changeLocale('ru');
  })

.controller('MainController',
  function MainController($scope, $location, $state) {
    let vm = this;
    
    $scope.$on('$stateChangeSuccess',
        function(event, toState, toParams, fromState, fromParams) {
          vm.bodyClass = $state.current.data.specialClass;
          vm.wrapperClass = $state.current.data.wrapperClass;
          vm.containerClass = $state.current.data.containerClass;
        });

});

