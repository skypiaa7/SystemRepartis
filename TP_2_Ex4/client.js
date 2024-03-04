const xmlrpc = require('xmlrpc');

const serverAddress = 'http://127.0.0.1:8000/RPC';

const client = xmlrpc.createClient({ host: '127.0.0.1', port: 8000, path: '/RPC' });

const expression = '2 + 3 * 4';

client.methodCall('calcul', [expression], (error, result) => {
    if (error) {
        console.error('Erreur lors de l\'appel à la méthode "calcul":', error);
    } else {
        console.log('Résultat de l\'évaluation:', result);
    }
});
