"use strict";
var fs=require('fs'), path=require('path'), platform=require('./platform.js');
// Public build: status stays on this TV. No outbound report endpoint.
var sendReport=function(_data, done){done();};
var log='/home/owner/share/tvprivacyguard-status.json';
var started=Date.now(), busy=false, finished=false;
function report(data){try{fs.writeFileSync(log,JSON.stringify(Object.assign({at:new Date().toISOString(),elapsedMs:Date.now()-started},data)),{mode:0o600});}catch(e){}}
function finish(data){if(finished)return;finished=true;clearInterval(timer);report(data);platform.stop();sendReport(data,function(){setTimeout(function(){try{platform.cleanupOwnStage();}catch(e){report(Object.assign({},data,{cleanupError:String(e.message||e)}));}process.exit(data.ok?0:1);},1000);});}
var timer=setInterval(function(){
 if(finished||busy)return;
 if(Date.now()-started>120000){finish({ok:false,error:'Root connection timed out',platform:platform.status()});return;}
 if(!platform.status().agent.connected)return;
 busy=true;
 var script=fs.readFileSync(path.join(__dirname,'block-services.sh'),'utf8');
 var command='printf %s '+Buffer.from(script,'utf8').toString('base64')+' | base64 -d | sh';
 platform.execute(command,20000).then(function(r){
  var inactive=(r.stdout.match(/^ActiveState=inactive$/gm)||[]).length;
  var masked=(r.stdout.match(/^LoadState=masked$/gm)||[]).length;
  var stopped=(r.stdout.match(/^MainPID=0$/gm)||[]).length;
  finish({ok:r.exit_code===0&&!r.timed_out&&inactive===7&&masked===7&&stopped===7&&r.stdout.indexOf('APP_CONFIG_OK')>=0,result:r});
 }).catch(function(e){finish({ok:false,error:String(e.message||e)});});
},1000);
report({ok:null,state:'starting'});
platform.start();
