'use strict';

var FetcherCtrl = ['$scope', '$http', function($scope, $http){
  var url = 'https://api.parse.com/1/classes/Checkout';
  var headers = {
    'X-Parse-Application-Id': 'AJDr9PL0vCWndW87pkoIgCaV9v5YJxzuaFTfpi0M',
    'X-Parse-REST-API-Key': 'r3mCXuXSTNQ7OHiX7u5jmLG5DPYWNQ7PTWNCXhNN'
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
