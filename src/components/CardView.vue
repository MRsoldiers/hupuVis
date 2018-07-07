<template>
  <div class="card">
    <div class="header">
      <div class="author">
        {{card.author}}
      </div>
      <div class="title">
        {{card.title}}
      </div>
    </div>
    <div class="content">
      <div class="word-cloud">
        <vue-word-cloud
          :words="words"
          :color="colorFunction"
          font-family="Roboto"
          :spacing="0.1"
        />
      </div>
      <div class="timeline" ref="timelineref">
        
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { Action, Getter, namespace } from 'vuex-class'
import { BindingHelpers } from 'vuex-class/lib/bindings'
import { ICard, ICardEntry, IHotpost } from '../store/modules/HupuStore/State'
import VueWordCloud from 'vuewordcloud'
import { maxBy, random } from 'lodash'
import { workers } from 'cluster';

const hupuStore: BindingHelpers = namespace('Hupu')

@Component({
  components: {
    [VueWordCloud.name]: VueWordCloud
  }
})
export default class CardView extends Vue {
    @Prop() public entry!: ICardEntry
    @Prop() public wordColor!: string[]

    private sdate: number = 2
    private tlWidth: number = 1
    private tlHeight: number = 1

    public get card(): ICard {
      return this.entry.card
    }

    public get maxWeight(): number {
      const maxWeightWord: [string, number]| undefined = maxBy(this.words, (w: [string, number]) => w[1])
      return maxWeightWord ? maxWeightWord[1] : 1
    }

    public colorFunction([, weight]: [string, number]): string {
      const colorIndex: number = random(0, this.wordColor.length - 1)
      return this.wordColor[colorIndex]
    }

    public get words(): [string, number][] {
      const words: [string, number][] = this.card.wordFrequency.sort((a: [string, number], b: [string, number]) => (a[1] - b[1]))
      const n: number = words.length > 15 ? 15 : words.length
      return words.slice(0, n)
    }

    // public get realTimeLine(): string[] {
    //   const hotposts: IHotpost[] = this.card.wellHotpost
    //   return hotposts.map((p: IHotpost) => {
    //     const time: string = p.time
    //     // '2018-07-03 20:25'
    //     const date = parseInt(time.slice(8,9))
    //     const h = parseInt(time.slice(11,12))
    //     const m = parseInt(time.slice(14,15))
    //     const pM = (date - this.sdate) * 24 * 60 + h * 60 + m
    //     return { pM, ...p }
    //   })
    // }

    private hackTimeSeries(): void {

    }

    private mounted(): void {
      const timeLineRect = (<HTMLElement>this.$refs.timelineref).getBoundingClientRect()
      this.tlWidth = timeLineRect.width
      this.tlHeight = timeLineRect.height
    } 

    // public get wordsRotated(): { text: string, weight: number, rotation: number }[] {
    //   const words: [string, number][] = this.card.wordFrequency.sort((a: [string, number], b: [string, number]) => (a[1] - b[1]))
    //   const n: number = words.length > 15 ? 15 : words.length
    //   return words.slice(0, n).map((w: [string, number]) => {
    //     return {
    //       text: w[0],
    //       weight: w[1],
    //       /* tslint:disable:insecure-random */
    //       rotation: Math.random() > 0.5 ? 0.75 : 0
    //     }
    //   })
    // }

}
</script>

<style lang="scss">
.card {
  margin-bottom: 10px;
  border-radius: 1px;
  border: 1px solid rgba(0,0,0,.125);
  height: 160px;
  width: calc(100% - 10px);
  overflow: hidden;

  .header {
    height: 25px;
    width: 100%;
    display: flex;
    background-color: #f7f7f7;
    border-bottom: 1px solid #ddd;

    .title {
      flex: 0 0 500px;
      font-family: Microsoft Yahei;
      line-height: 24px;
      font-size: 18px;
      font-weight: 600;
      margin: 0px 4px;
      text-align: start;
      overflow: hidden;
      text-overflow: ellipsis;
      color: #777;
      white-space: nowrap;
    }

    .author {
      flex: 0 0 100px;
      font-family: Microsoft Yahei;
      line-height: 24px;
      font-size: 14px;
      font-weight: 500;
      overflow: hidden;
      text-overflow: ellipsis;
      text-align: start;
      margin: 0px 4px;
      color: #888;
    }
  }

  .content {
    position: relative;
    width: calc(100%);
    height: calc(100% - 25px);
    display: flex;

    .word-cloud {
      flex: 0 0 200px;
      padding: 15px;
    }

    .timeline {
      flex: 1 1;
      background-color: #f1f1f1;
      border-left: 1px solid #ddd;
    }

  }
}
</style>
