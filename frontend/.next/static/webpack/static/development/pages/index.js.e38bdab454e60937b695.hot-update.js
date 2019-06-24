webpackHotUpdate("static/development/pages/index.js",{

/***/ "./components/Results.js":
/*!*******************************!*\
  !*** ./components/Results.js ***!
  \*******************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");
/* harmony import */ var styled_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! styled-components */ "./node_modules/styled-components/dist/styled-components.browser.esm.js");
var _jsxFileName = "/Users/liamz/Documents/open-source/retrust/frontend/components/Results.js";



var VoteIcon = styled_components__WEBPACK_IMPORTED_MODULE_2__["default"].i.withConfig({
  displayName: "Results__VoteIcon",
  componentId: "sc-1a3mvwk-0"
})(["font-size:18px;:hover{cursor:pointer;transform:translate3d(10px,-10px):}"]);
var VotePane = styled_components__WEBPACK_IMPORTED_MODULE_2__["default"].div.withConfig({
  displayName: "Results__VotePane",
  componentId: "sc-1a3mvwk-1"
})(["display:inline-flex;flex-direction:column;text-align:center;padding-right:1em;"]);
var ResultBody = styled_components__WEBPACK_IMPORTED_MODULE_2__["default"].div.withConfig({
  displayName: "Results__ResultBody",
  componentId: "sc-1a3mvwk-2"
})(["display:inline-flex;align-self:center;font-size:16px;"]);
var ResultStyle = styled_components__WEBPACK_IMPORTED_MODULE_2__["default"].div.withConfig({
  displayName: "Results__ResultStyle",
  componentId: "sc-1a3mvwk-3"
})(["display:flex;margin:1em 0.25em;"]);
var Total = styled_components__WEBPACK_IMPORTED_MODULE_2__["default"].span.withConfig({
  displayName: "Results__Total",
  componentId: "sc-1a3mvwk-4"
})([""]);

function Results(_ref) {
  var results = _ref.results;
  return react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
    __source: {
      fileName: _jsxFileName,
      lineNumber: 35
    },
    __self: this
  }, results.map(Result));
}

function Result(_ref2) {
  var total = _ref2.total,
      link = _ref2.link;
  return react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(ResultStyle, {
    __source: {
      fileName: _jsxFileName,
      lineNumber: 41
    },
    __self: this
  }, react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(VotePane, {
    __source: {
      fileName: _jsxFileName,
      lineNumber: 43
    },
    __self: this
  }, react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(VoteIcon, {
    className: "fas fa-arrow-up",
    __source: {
      fileName: _jsxFileName,
      lineNumber: 44
    },
    __self: this
  }), react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(Total, {
    __source: {
      fileName: _jsxFileName,
      lineNumber: 45
    },
    __self: this
  }, total), react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(VoteIcon, {
    className: "fas fa-arrow-down",
    __source: {
      fileName: _jsxFileName,
      lineNumber: 46
    },
    __self: this
  })), react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(ResultBody, {
    __source: {
      fileName: _jsxFileName,
      lineNumber: 49
    },
    __self: this
  }, link));
}

/* harmony default export */ __webpack_exports__["default"] = (Object(react_redux__WEBPACK_IMPORTED_MODULE_1__["connect"])()(Results));

/***/ })

})
//# sourceMappingURL=index.js.e38bdab454e60937b695.hot-update.js.map