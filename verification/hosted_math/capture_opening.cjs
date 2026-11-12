'use strict';
// Supplement full-page captures when GitHub's sticky toolbar overlaps content.
// Fresh, unsigned-in opening views; no page styling or TeX is injected.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {chromium}=require('playwright');
const {argumentsFor,pinnedPages}=require('./capture_hosted_math.cjs');
async function main(){
  const args=argumentsFor(process.argv.slice(2)),out=path.resolve(args.output);
  if(fs.existsSync(out)&&fs.readdirSync(out).length)throw Error('Use a new evidence directory');
  fs.mkdirSync(out,{recursive:true});
  const pin=pinnedPages(args),browser=await chromium.launch({headless:true}),captures=[];
  try{
    for(const width of [1440,760]){
      const context=await browser.newContext({viewport:{width,height:1800}});
      try{
        for(const [i,p] of pin.pages.entries()){
          const page=await context.newPage();
          try{
            const url=`https://github.com/${args.repository}/blob/${args.revision}/${p}`;
            const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:60000});
            if(response.status()!==200||page.url()!==url)throw Error('Exact hosted source unavailable');
            await page.locator('article.markdown-body').waitFor({state:'visible'});
            await page.waitForFunction(()=>{
              const a=document.querySelector('article.markdown-body');
              const hosts=[...a.querySelectorAll('math-renderer')].filter(x=>{
                const r=x.getBoundingClientRect();return r.top<innerHeight&&r.bottom>0;
              });
              return hosts.every(x=>x.querySelector('math')&&!x.querySelector('[data-mjx-error],mjx-merror'));
            },null,{timeout:30000});
            await page.evaluate(async()=>{await document.fonts.ready;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));});
            const file=`opening-${String(i+1).padStart(4,'0')}-${width}.png`;
            await page.screenshot({path:path.join(out,file),fullPage:false});
            const bytes=fs.readFileSync(path.join(out,file));
            captures.push({path:p,url,revision:args.revision,width,height:1800,file,size_bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex'),observed_at:new Date().toISOString()});
          }finally{await page.close();}
        }
      }finally{await context.close();}
    }
  }finally{await browser.close();}
  fs.writeFileSync(path.join(out,'opening-report.json'),JSON.stringify({repository:args.repository,revision:args.revision,tree:pin.tree,method:'fresh-hosted-opening-viewport',captures},null,2)+'\n');
}
main().catch(e=>{console.error(String(e));process.exitCode=1;});
