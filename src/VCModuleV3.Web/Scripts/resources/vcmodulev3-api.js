angular.module('VCModuleV3')
    .factory('VCModuleV3.api', ['$resource', function ($resource) {
        return $resource('api/VCModuleV3');
    }]);
