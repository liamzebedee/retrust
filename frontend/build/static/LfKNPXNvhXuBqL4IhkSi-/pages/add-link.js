(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{BBPJ:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/add-link",function(){var e=n("hb5Z");return{page:e.default||e}}])},CIUX:function(e,t,n){"use strict";var a=n("vOnD").a.button.withConfig({displayName:"Button",componentId:"sc-6z615l-0"})(["border-radius:1px;padding:0.5em;:hover{cursor:pointer;background:#eee;color:black;border-color:1px solid black;}"]);t.a=a},hb5Z:function(e,t,n){"use strict";n.r(t);var a=n("q1tI"),i=n.n(a),o=n("3uVX"),l=n("CIUX"),r=n("vOnD"),d=n("doui"),c=n("zrwo"),u=n("/MKj"),s=r.a.div.withConfig({displayName:"TxStatusWidget__TxTracker",componentId:"wh1fqe-0"})(["font-size:12px;margin:1em 0em;"]);var m=Object(u.b)(function(e,t){var n=e.txs[t.txhash];return Object(c.a)({},n)},function(e,t){return{}})(function(e){var t=e.status,n=e.txhash;if(!n)return null;var o,l=Object(a.useState)(!1),r=Object(d.default)(l,2),c=r[0],u=r[1];switch(t){case"processing":o=i.a.createElement("i",{class:"fab fa-buffer"});case"confirmed":o=i.a.createElement("i",{class:"fas fa-check-circle"})}return i.a.createElement(s,null,i.a.createElement("span",{onClick:function(){return u(!0)}},"tx ",c&&n),": ",o)}),p=r.a.h2.withConfig({displayName:"AddLink__Title",componentId:"w723ak-0"})(["font-size:24px;"]),f=r.a.div.withConfig({displayName:"AddLink__AddEntryStyle",componentId:"w723ak-1"})(["margin:3em auto;width:600px;"]),h=r.a.div.withConfig({displayName:"AddLink__FormRow",componentId:"w723ak-2"})(["display:flex;justify-content:flex-end;padding:1em 0;:nth-child(1){padding-top:0;}flex-direction:column;label{padding:.5em 1em .5em 0;flex:1;font-weight:bold;}input{height:50px;}textarea{outline:none;resize:none;overflow:auto;border:1px solid #333;padding:1em;}"]);r.a.input.withConfig({displayName:"AddLink__URLInput",componentId:"w723ak-3"})(["height:75px;"]);var g=function(e){var t=e.submit,n=e.txhash,r=Object(a.useState)(),c=Object(d.default)(r,2),u=c[0],s=c[1],g=Object(a.useState)(),b=Object(d.default)(g,2),x=b[0],w=b[1],v=Object(a.useState)(!1),E=Object(d.default)(v,2),k=E[0],y=E[1];return i.a.createElement(o.a,null,i.a.createElement(f,null,i.a.createElement(p,null,"Add link ",i.a.createElement("i",{className:"fas fa-link"})),i.a.createElement("p",null,"Your contribution is stored ",i.a.createElement("i",null,"*forever*")," and can't be removed."),i.a.createElement(h,null,i.a.createElement("label",null,"Entry name"),i.a.createElement("textarea",{type:"text",onChange:function(e){return s(e.target.value)},placeholder:"eg. Bitcoin: A Peer-to-Peer Electronic Cash System",value:u})),i.a.createElement(h,{style:{paddingTop:0}},i.a.createElement("label",null,"URL"),i.a.createElement("textarea",{type:"text",value:x,onChange:function(e){return w(e.target.value)},placeholder:"https, magnet, torrent and ipfs links go here"})),i.a.createElement(h,null,i.a.createElement(l.a,{onClick:function(){y(!0),t(u,x)}},"Submit"),k?i.a.createElement(m,{txhash:n}):null)))},b=n("2AN/");var x=Object(u.b)(function(e,t){return{txhash:e.registry.addToRegistry}},function(e,t){return{submit:function(t,n){e(Object(b.e)(t,n))}}})(function(e){return i.a.createElement(g,e)});r.a.h2.withConfig({displayName:"add-link__Title",componentId:"sc-1sv4a7z-0"})(["font-size:24px;"]),r.a.div.withConfig({displayName:"add-link__AddEntryStyle",componentId:"sc-1sv4a7z-1"})(["margin:3em auto;width:600px;"]),r.a.div.withConfig({displayName:"add-link__FormRow",componentId:"sc-1sv4a7z-2"})(["display:flex;justify-content:flex-end;padding:1em 0;:nth-child(1){padding-top:0;}flex-direction:column;label{padding:.5em 1em .5em 0;flex:1;font-weight:bold;}input{height:50px;}textarea{outline:none;resize:none;overflow:auto;border:1px solid #333;padding:1em;}"]),r.a.input.withConfig({displayName:"add-link__URLInput",componentId:"sc-1sv4a7z-3"})(["height:75px;"]);t.default=x}},[["BBPJ",1,0]]]);