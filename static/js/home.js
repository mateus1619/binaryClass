

$('.demo').squeezebox({
  timing:300
});



// quando clicar em algum item no accordion
accordion = document.getElementById('squeezecnt')
accordion.addEventListener('click', (e)=>{

  (async () =>{
    try {
      const response = await fetch('/videos/' + id.toString());

      if (!response.ok) {
        throw new Error('Erro ao obter os dados');
      }

      const data = await response.json();

      let id = e.target.id
      let videoSources = new Array();
      let videoQuality = new Array();

      for(const element of data.videos){
        // fps = element.fps
        // progressive = element.progressive
        reso = element.resolution
        url = element.url

        videoSources.push({src: url,type: 'video/mp4',size: reso});
        videoQuality.push(parseInt(reso))
      }

      const player = new Plyr('#player', {
        quality: {
          default: 360,
          options: videoQuality
        }
      });
      player.config.quality = {default: 360,options: [720, 360]}
      console.log(player)
      player.source = {
        type: 'video',
        title: 'Example title',
        sources: videoSources,
        poster: 'https://cdn.plyr.io/static/demo/View_From_A_Blue_Moon_Trailer-HD.jpg',
        previewThumbnails: {
          src: '/path/to/thumbnails.vtt',
        }
      };
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  })();

});

// const player = new Plyr('#player', {

// });


// Expose player so it can be used from the console
// window.player = player;