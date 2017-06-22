/**
 * Copyright 2016, GeoSolutions Sas.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
const axios = require('../../MapStore2/web/client/libs/ajax');
const ConfigUtils = require('../../MapStore2/web/client/utils/ConfigUtils');
const assign = require('object-assign');
const dataCache = {};

const getLayerId = (properties) => {
    let layerId = "";
    if (properties.occurrence_cat[0] === 'plant') {
        layerId = 'plants';
    } else if (properties.occurrence_cat[0] === 'animal') {
        layerId = 'animals';
    }
    return layerId;
};

const Api = {
    addBaseUrl: function(options) {
        return assign(options, {baseURL: ConfigUtils.getDefaults().geoStoreUrl});
    },
    getData: function(url) {
        const cached = dataCache[url];
        if (cached && new Date().getTime() < cached.timestamp + (ConfigUtils.getConfigProp('cacheDataExpire') || 60) * 1000) {
            return new Promise((resolve) => {
                resolve(cached.data);
            });
        }
        return axios.get(url).then((response) => {
            dataCache[url] = {
                timestamp: new Date().getTime(),
                data: response.data
            };
            return response.data;
        });
    },
    updateNaturalFeature: function(id, feature) {
        let url = "users/user/" + id;
        return axios.put(url, {NaturalFeature: feature}, this.addBaseUrl()).then(function(response) {return response.data; });
    },
    saveNaturalFeature: function(id, feature) {
        let url = "users/user/" + id;
        return axios.put(url, {NaturalFeature: feature}, this.addBaseUrl()).then(function(response) {return response.data; });
    },
    deleteNaturalFeature: function(id, feature) {
        let url = "users/user/" + id;
        return axios.put(url, {NaturalFeature: feature}, this.addBaseUrl()).then(function(response) {return response.data; });
    },
    getFeatureType: function(properties, nfid) {
        let url = 'http://geosolutions.scolab.eu/nfdapi/featuretypes/' + getLayerId(properties) + '/' + nfid;
        return axios.get(url).then(function(response) {return response.data; });
    }
};

module.exports = Api;
