'use strict';

var FetcherCtrl = ['$scope', '$http', function($scope, $http){
  var url = 'https://api.parse.com/1/classes/Checkout';
  var headers = {
    'X-Parse-Application-Id': 'ElAH6C9vFmBLeO09O5qD0PgUfX0bA6v2zqiGap1L',
    'X-Parse-REST-API-Key': 'HmBjwglSnpTmzzGK3BRqtu5zD1LQndTbH8LJde1f'
  };
  var params = {
    "order": "-createdAt"
  };
  $scope.commits = {};
  $http.get(url, {headers: headers, params: params}).success(function(data, success){
    angular.forEach(data.results, function(val){
      if (!$scope.commits[val.user_email]) $scope.commits[val.user_email] = [];
      $scope.commits[val.user_email].push(val);
    });
  });
}];
