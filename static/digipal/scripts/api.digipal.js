/**
 ** Digipal API
 ** @options {Object}
 **/

function DigipalAPI(options) {

    var self = this;

    var default_options = {
        crossDomain: true,
        root: 'http://localhost:8000/digipal/api' // will be http://www.digipal.eu/digipal/api
    };

    /*
     ** Utils
     */

    var utils = {

        extend: function() {
            var out = out || {};
            for (var i = 1; i < arguments.length; i++) {
                if (!arguments[i]) {
                    continue;
                }
                for (var key in arguments[i]) {
                    if (arguments[i].hasOwnProperty(key))
                        out[key] = arguments[i][key];
                }
            }
            return out;
        },

        getCookie: function(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },

        serializeObject: function(_object) {
            var s = '';
            var n = 0;
            for (var i in _object) {
                if (n >= 1) {
                    s += '&';
                }
                s += '_' + i + '=' + _object[i];
                n++;
            }
            return s;
        }
    };

    /*
     ** the default options get extended with those selected at initialization
     */

    default_options = utils.extend({}, default_options, options);

    var constants = {
        ROOT: default_options.root,
        DATATYPES: ['graph', 'allograph', 'hand', 'scribe', 'allograph', 'idiograph', 'annotation', 'component', 'feature', 'image']
    };

    /*
     ** function to return public methods
     */

    var init = function() {
        var functions = generateFunctions();
        return functions;
    };

    /*
     ** Function to dynamically create methods based on constants.DATATYPES
     */

    var generateFunctions = function() {
        var functions = {};
        for (var i = 0; i < constants.DATATYPES.length; i++) {
            var datatype = constants.DATATYPES[i];
            (function(datatype) {
                functions[datatype] = function(url, callback, select, limit) {
                    url = process_url(url, select, limit);
                    return request(constants.ROOT + '/' + datatype + '/' + url, callback, select);
                };
            })(datatype);
        }

        return functions;
    };

    /*
     ** Function to inject JSONP script
     ** for @url parameter see @request
     */

    var makeRequestScript = function(url) {
        var script = document.createElement('script');
        var head = document.head;
        script.setAttribute("src", url);
        script.setAttribute("async", true);
        head.appendChild(script);
        return script;
    };

    /*
     ** AJAX call if calls get done on the same domain
     ** for parameters see @request
     */

    var Ajax = function(url, callback) {
        var xmlhttp;
        var csrftoken = utils.getCookie('csrftoken');

        if (window.XMLHttpRequest) {
            // code for IE7+, Firefox, Chrome, Opera, Safari
            xmlhttp = new XMLHttpRequest();
        } else {
            // code for IE6, IE5
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }

        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                callback(xmlhttp.responseText);
            }
        };

        xmlhttp.open("GET", url, true);
        xmlhttp.setRequestHeader("Content-type", "application/json");
        xmlhttp.send('csrftoken=' + csrftoken);

    };

    var process_url = function(url, select, limit) {

        if (url instanceof Array) {
            url = url.toString();
        } else if (url instanceof Object) {
            url = '?' + utils.serializeObject(url);
        }

        if (typeof select !== 'undefined' && select.length) {
            url += "&@select=" + select.toString();
        }

        if (typeof limit !== 'undefined' && limit) {
            url += '&@limit=' + limit;
        }
        return url;
    };

    /*
     ** Request function
     ** @url = {Number} : id of the resource,
     ** @url = {Array} : array of ids of the resource,
     ** @url = {Object} : list of fields {field: value, field2 : value2} (see @constants.DATATYPES)
     ** @callback = {Function} : function to be executed when the call finishes
     ** @select: {Array} : array of fields (see @constants.DATATYPES) to be pulled. If undefined, all fields get called
     */

    var request = function(url, callback) {

        /*
         ** JSONP request
         */

        if (default_options.crossDomain) {
            var cb = '_callback';
            url += '?callback=' + cb;
            var script = makeRequestScript(url);
            window[cb] = function(data) {
                callback(success, message, data);
                window[cb] = null;
                delete window[cb];
                script.parentNode.removeChild(script);
            };
        } else {
            Ajax(url, callback);
        }

    };

    /*
     ** Return public methods generated by @generateFunctions to the object
     */

    return (function() {
        return init();
    })();
}