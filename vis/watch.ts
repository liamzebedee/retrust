
import * as chokidar from 'chokidar';

import * as path from 'path';

import * as nrc from 'node-run-cmd';

const spawn = require('child_process').spawn;

class Watcher {
    constructor(){}
    async watch(): Promise<any> {
        const glob = require("glob");
        
        chokidar.watch(
            // glob.glob("networks/*.txt")
            path.join('./networks/*.interactions')
        ).on('all', (event: string, fpath: string) => {
            if(!['change', 'add'].includes(event)) {
                return;
            }
    
            let fname = path.parse(fpath).base;
            this.onFileUpdate(fname, fpath);
        });
    }
    
    onFileUpdate(fname: string, fpath: string) {
        console.log(fname, fpath)
        // nrc.run(`python vis/vis_graphs.py ${fpath}`)
        spawn('python', `vis/main.py render --graph-path ${fpath}`.split(' '), { stdio: 'inherit' });
    }
}

const watcher = new Watcher;
watcher.watch()