import json,sys,subprocess,shutil,os,glob,math,random,wave,struct
from playwright.sync_api import sync_playwright
spec=json.load(open(sys.argv[1])); out=sys.argv[2]
sl=spec['slides']; n=len(sl); T=0.4; FPS=30; W,H=1080,1920
FR=os.path.join(out,'_frames'); shutil.rmtree(FR,ignore_errors=True); os.makedirs(FR)
ANIM="""<style id='anim'>
@keyframes up{from{opacity:0;transform:translateY(46px)}to{opacity:1;transform:none}}
@keyframes slapk{0%{opacity:0;transform:rotate(-1.6deg) scale(1.7)}60%{opacity:1;transform:rotate(-1.6deg) scale(.94)}100%{transform:rotate(-1.6deg) scale(1)}}
@keyframes drop{0%{opacity:0;transform:translateY(-170px) rotate(-7deg) scale(1.06)}70%{opacity:1;transform:translateY(8px) rotate(.6deg)}100%{transform:none}}
@keyframes draw{to{stroke-dashoffset:0}}
@property --a{syntax:'<angle>';inherits:false;initial-value:0deg}
@keyframes ring{from{--a:0deg}to{--a:361deg}}
@keyframes penin{from{transform:translate(-320px,240px) rotate(-34deg)}to{transform:rotate(-16deg)}}
@keyframes slapp{0%{opacity:0;transform:rotate(16deg) scale(1.55) translateY(-70px)}65%{opacity:1;transform:rotate(4deg) scale(.96)}100%{transform:rotate(6deg) scale(1)}}
@keyframes thump{0%{opacity:0;transform:rotate(-5deg) scale(2.6)}55%{opacity:.95;transform:rotate(-5deg) scale(.95)}100%{opacity:.9;transform:rotate(-5deg) scale(1)}}
@keyframes shake{0%,100%{transform:none}20%{transform:translate(7px,-5px)}45%{transform:translate(-6px,4px)}70%{transform:translate(3px,-2px)}}
@keyframes pop{0%{opacity:0;transform:scale(.6)}70%{opacity:1;transform:scale(1.06)}100%{transform:scale(1)}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1) rotate(-.6deg)}}
@keyframes growy{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes pin{0%{opacity:0;transform:translateY(-60px) scale(1.3)}70%{opacity:1;transform:translateY(4px) scale(.97)}100%{transform:none}}
@keyframes tapein{from{transform:translateX(-1400px) rotate(-6deg)}to{transform:rotate(-6deg)}}
@keyframes rulin{from{transform:translateX(-90px) rotate(.6deg)}to{transform:rotate(.6deg)}}
@keyframes cote{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes sweep{from{transform:translateX(-120%)}to{transform:translateX(120%)}}
@keyframes bmd{0%{opacity:0;transform:translateY(-140px)}70%{opacity:1;transform:translateY(10px)}100%{transform:none}}
.kick{animation:slapk .45s .05s both cubic-bezier(.2,.9,.3,1)}
.t{animation:up .55s .2s both cubic-bezier(.2,.8,.2,1)} .in.hk .t{animation:none}
.p,.bigl{animation:up .5s .55s both cubic-bezier(.2,.8,.2,1)}
.dwrap{animation:drop .6s .4s both cubic-bezier(.2,.8,.3,1)} .in.hk .dwrap{animation-delay:.15s}
.hand{-webkit-mask-image:conic-gradient(from 150deg,#000 var(--a),transparent 0);mask-image:conic-gradient(from 150deg,#000 var(--a),transparent 0);animation:ring .85s 1.05s both cubic-bezier(.45,.05,.4,1)}
.penw{animation:penin .7s .75s both cubic-bezier(.2,.8,.2,1)}
.postit{animation:slapp .42s 1.75s both cubic-bezier(.2,.9,.3,1)}
.stamp{animation:thump .3s 2.15s both cubic-bezier(.3,.7,.3,1)}
.s.hasstamp{animation:shake .3s 2.28s both}
.swipe{animation:pop .4s 2.5s both}
.big{animation:pop .5s .15s both}
.bar .bf{transform-origin:left center;animation:grow .7s 1s both cubic-bezier(.2,.8,.2,1)}
.bar:nth-child(2) .bf{animation-delay:1.35s} .bar:nth-child(3) .bf{animation-delay:1.7s}
.st::before{transform-origin:top;animation:growy 1.4s .7s both linear}
.sp{animation:pin .45s .7s both cubic-bezier(.2,.9,.3,1)} .sp:nth-child(2){animation-delay:1.25s} .sp:nth-child(3){animation-delay:1.8s}
.tape{animation:tapein .55s 2.3s both cubic-bezier(.2,.8,.2,1)}
.ruler{animation:rulin .5s 0s both cubic-bezier(.2,.8,.2,1)}
.cote{transform-origin:left;animation:cote .9s .1s both cubic-bezier(.3,.6,.2,1)}
.card{animation:drop .6s .45s both cubic-bezier(.2,.8,.3,1)}
.it .tick path{stroke-dasharray:1;stroke-dashoffset:1;animation:draw .35s 1.15s both}
.it:nth-of-type(3) .tick path{animation-delay:1.6s} .it:nth-of-type(4) .tick path{animation-delay:2.05s}
.tr{animation:drop .55s .5s both} .tr:nth-child(3){animation-delay:1.1s} .tr:nth-child(4){animation-delay:1.7s}
.bm{animation:bmd .55s .1s both cubic-bezier(.2,.9,.3,1)}
.save{animation:pop .45s .95s both}
.sweep{position:absolute;inset:0;z-index:7;pointer-events:none;background:linear-gradient(104deg,transparent 38%,rgba(255,255,255,.13) 50%,transparent 62%);mix-blend-mode:screen;animation:sweep 2.4s .3s both ease-in-out}
</style>"""
JS="""<script>
document.querySelectorAll('.tick path').forEach(p=>p.setAttribute('pathLength','1'));
const S=document.querySelector('.s'); if(document.querySelector('.stamp')) S.classList.add('hasstamp');
const sw=document.createElement('div'); sw.className='sweep'; S.appendChild(sw);
const B=document.querySelector('.big'); const bo=B?B.textContent:'';
window.__end=()=>Math.max(0,...document.getAnimations().map(a=>a.effect.getComputedTiming().endTime))/1000;
window.__seek=(t)=>{document.getAnimations().forEach(a=>{a.pause();a.currentTime=t*1000});
 if(B&&bo.indexOf(',')<0){const d=bo.replace(/[^0-9]/g,''); if(d){let k=0; for(let j=0;j<bo.length;j++){if(bo[j]>='0'&&bo[j]<='9')k=j}
  const v=parseInt(d); const q=Math.min(1,Math.max(0,(t-.25)/1.0)); const e=1-Math.pow(1-q,3);
  B.textContent=Math.round(v*e).toLocaleString('fr-FR')+bo.slice(k+1)}}};
</script>"""
def readtime(i,s):
    txt=' '.join(str(v) for k,v in s.items() if k in ('title','text','number','label','save','offer'))
    txt+=' '+' '.join(s.get('items',[])+s.get('rows',[])+s.get('steps',[]))
    words=len(txt.replace('|',' ').split())
    return 2.4 if i==1 else min(4.6,max(2.6,0.9+words/3.8))
durs=[]
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':W,'height':H})
    for i,s in enumerate(sl,1):
        h=open(f'{out}/slide{i}.html').read().replace('</body>',ANIM+JS+'</body>')
        pg.set_content(h); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        A=pg.evaluate('window.__end()')
        dd=max(readtime(i,s),A+1.0)+(1.2 if i==n else 0); durs.append(round(dd,2))
        nf=int(math.ceil(A*FPS))+1
        for k in range(nf):
            pg.evaluate(f'window.__seek({k/FPS})'); pg.screenshot(path=f'{FR}/s{i}_{k:04d}.jpg',type='jpeg',quality=93)
    br.close()
ff=shutil.which('ffmpeg')
if not ff:
    subprocess.run(['pip','install','-q','imageio-ffmpeg','--break-system-packages'],check=True)
    import imageio_ffmpeg; ff=imageio_ffmpeg.get_ffmpeg_exe()
SR=44100; total=sum(durs)+T+0.5; N=int(total*SR); buf=[0.0]*N; rnd=random.Random(3)
def add(t0,dur,fn,amp):
    a=int(t0*SR)
    for j in range(int(dur*SR)):
        if 0<=a+j<N: buf[a+j]+=amp*fn(j/SR,dur)
def noise_env(attack,decay):
    st={'lp':0.0}
    def f(t,d):
        st['lp']=st['lp']*0.6+rnd.uniform(-1,1)*0.4
        e=min(1,t/attack)*math.exp(-t/decay); return st['lp']*e
    return f
def thump(t,d): return math.sin(2*math.pi*(95-40*t)*t)*math.exp(-t/0.07)+rnd.uniform(-1,1)*0.25*math.exp(-t/0.02)
def scribble(t,d): return rnd.uniform(-1,1)*(0.55+0.45*math.sin(2*math.pi*9*t))*min(1,t/0.05)*min(1,(d-t)/0.08)
off=0.0; starts=[]
for i,dd in enumerate(durs): starts.append(off); off+=dd
for i,s in enumerate(sl):
    t0=starts[i]; ty=s.get('type')
    if i>0: add(t0-0.05,0.35,noise_env(0.12,0.12),0.10)
    if ty in ('hook','doc'):
        add(t0+0.42,0.4,noise_env(0.01,0.09),0.22)
        add(t0+1.05,0.8,scribble,0.05)
        d=s.get('doc',{})
        if d.get('note'): add(t0+1.78,0.25,noise_env(0.005,0.04),0.25)
        if d.get('stamp'): add(t0+2.2,0.35,thump,0.6)
    if ty=='card' or ty=='check': add(t0+0.48,0.4,noise_env(0.01,0.09),0.2)
    if ty=='steps':
        for dl in (0.75,1.3,1.85): add(t0+dl,0.2,thump,0.18)
        add(t0+2.3,0.5,noise_env(0.03,0.15),0.12)
    if ty=='end': add(t0+0.5,0.25,thump,0.15)
wf=wave.open(f'{out}/_sfx.wav','wb'); wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
wf.writeframes(b''.join(struct.pack('<h',int(max(-1,min(1,v))*30000)) for v in buf)); wf.close()
cmd=[ff,'-y','-loglevel','error']
for i,dd in enumerate(durs,1): cmd+=['-framerate',str(FPS),'-i',f'{FR}/s{i}_%04d.jpg']
cmd+=['-i',f'{out}/_sfx.wav']
f=[]
for i,dd in enumerate(durs):
    nf=len(glob.glob(f'{FR}/s{i+1}_*.jpg')); hold=max(0.1,dd+T-nf/FPS); tot=int((dd+T)*FPS)
    f.append(f"[{i}:v]tpad=stop_mode=clone:stop_duration={hold:.2f},scale=1620:2880,zoompan=z='1.035+0.03*on/{tot}':x='iw/2-(iw/zoom/2)+12*sin(on/23+{i})+4*sin(on/7.3)':y='ih/2-(ih/zoom/2)+15*sin(on/29+{2*i})+4*sin(on/8.1)':d=1:s=1080x1920:fps={FPS},setsar=1[z{i}]")
prev='z0'; off=0.0
for k in range(1,n):
    off+=durs[k-1]; lab=f'v{k}'
    f.append(f'[{prev}][z{k}]xfade=transition=slideleft:duration={T}:offset={off:.2f}[{lab}]'); prev=lab
f.append(f"[{prev}]noise=alls=7:allf=t+u,vignette=angle=0.5,eq=brightness='0.012*sin(2*PI*t*0.6)':eval=frame,format=yuv420p[vout]")
cmd+=['-filter_complex',';'.join(f),'-map','[vout]','-map',f'{n}:a','-shortest','-c:v','libx264','-preset','medium','-crf','19','-r',str(FPS),'-c:a','aac','-b:a','128k','-movflags','+faststart',f'{out}/reel.mp4']
subprocess.run(cmd,check=True)
shutil.rmtree(FR,ignore_errors=True); os.remove(f'{out}/_sfx.wav')
print('reel.mp4',round(sum(durs)+T,1),'s',durs)
