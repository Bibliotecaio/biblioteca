/**
 * This file/module contains all configuration for the build process.
 */
module.exports = {
  /**
   * The `buildDir` folder is where our projects are compiled during
   * development and the `compileDir` folder is where our app resides once it's
   * completely built.
   */
  buildDir: 'build',
  compileDir: 'bin',

  devEnv: {
    name: 'development',
    apiEndpoint: 'http://localhost:8000',
    fileStorageEndpoint: 'http://localhost:9333',
    fillerStorageEndpoint: 'http://localhost:8888',
    uploadMimeTypes: [
      'application/pdf'
    ]
  },

  prodEnv: {
    name: 'production',
    apiEndpoint: 'https://api.kniznica.ru',
    fileStorageEndpoint: 'https://storage.kniznica.ru',
    fillerStorageEndpoint: 'https://storage.kniznica.ru/files',
    uploadMimeTypes: [
      'application/pdf'
    ]
  },

  /**
   * This is a collection of file patterns that refer to our app code (the
   * stuff in `src/`). These file paths are used in the configuration of
   * build tasks. `js` is all project javascript, less tests. `ctpl` contains
   * our reusable components' (`src/common`) template HTML files, while
   * `atpl` contains the same, but for our app's code. `html` is just our
   * main HTML file, `less` is our main stylesheet, and `unit` contains our
   * app's unit tests.
   */
  appFiles: {
    js: ['src/**/*.js', '!src/**/*.spec.js', '!src/assets/**/*.js', '!src/plugins/**/*.js' ],

    atpl: [ 'src/app/**/*.tpl.html' ],
    ctpl: [ 'src/common/**/*.tpl.html' ],

    html: [ 'src/index.html' ],
    less: 'src/less/style.less'
  },

  /**
   * This is a collection of files used during testing only.
   */
  testFiles: {
    js: [
    ]
  },

  /**
   * This is the same as `appFiles`, except it contains patterns that
   * reference vendor code (`vendor/`) that we need to place into the build
   * process somewhere. While the `appFiles` property ensures all
   * standardized files are collected for compilation, it is the user's job
   * to ensure non-standardized (i.e. vendor-related) files are handled
   * appropriately in `vendorFiles.js`.
   *
   * The `vendorFiles.js` property holds files to be automatically
   * concatenated and minified with our project source files.
   *
   * The `vendorFiles.css` property holds any CSS files to be automatically
   * included in our app.
   *
   * The `vendorFiles.assets` property holds any assets to be copied along
   * with our app's assets. This structure is flattened, so it is not
   * recommended that you use wildcards.
   */
  vendorFiles: {
    js: [
      "vendor/jquery/dist/jquery.min.js",
      "vendor/jquery-ui/jquery-ui.min.js",
      "vendor/bootstrap/dist/js/bootstrap.min.js",
      "vendor/metisMenu/dist/metisMenu.min.js",
      "vendor/slimScroll/jquery.slimscroll.min.js",
      "vendor/pace/pace.min.js",
      "vendor/angular/angular.min.js",
      "vendor/angular-ui-router/release/angular-ui-router.min.js",
      "vendor/angular-bootstrap/ui-bootstrap-tpls.min.js",
      'vendor/angular-resource/angular-resource.min.js',
      'vendor/angular-local-storage/dist/angular-local-storage.min.js',
      'vendor/angularjs-toaster/toaster.min.js',
      'vendor/angular-filter/dist/angular-filter.min.js',
      'vendor/moment/moment.js',
      'vendor/moment/locale/ru.js',
      'vendor/angular-moment/angular-moment.min.js',
      'vendor/angular-file-upload/dist/angular-file-upload.min.js',
      'vendor/ng-text-truncate/ng-text-truncate.js',
      'vendor/ngSticky/dist/sticky.min.js',
      'vendor/angular-sanitize/angular-sanitize.min.js',
      'vendor/angular-ui-select/dist/select.min.js',
      
    ],
    css: [
      //'vendor/fontawesome/css/font-awesome.css',
      //'vendor/bootstrap/dist/css/bootstrap.min.css',
      'vendor/angularjs-toaster/toaster.min.css',
      'vendor/angular-ui-select/dist/select.min.css'

      
    ],
    fonts: [
      //'vendor/bootstrap/fonts/*',
      //'vendor/fontawesome/fonts/*'
    ],
    assets: [
        'images',
        'fonts'
    ]
  },
  themeFiles: {
    css: [
      'src/styles/animate.min.css'
    ]
  },
  
  viewerFiles: {
    js: [
      'src/plugins/document-viewer/js/*'
    ],
    css: [
      'src/plugins/document-viewer/css/*'
    ]
  },
  
  icheckFiles: {
    js: [
      'src/plugins/iCheck/*'
    ]
  },
  
  cache : {
    manifest: [
      'src/cache.manifest'
    ]
  }
  
};
