<template>
  <div class="hupu-view">
    <div class="nav" @click="showCards()">
    </div>
    <div class="card-list-cont">
      <div class="card-list">
        <card-view v-for="c in cardEntries" :key="c.index" :wordColor="wordColor"
          :entry=c></card-view>
      </div>
      <div class="panel">
        <div class="color-panel">
          <div class="color-btn" v-for="(wc, index) in wordColors" :key="index"
            :class="{ selected: index === wordColorIndex, hovering: index === hoveringColorBtn }"
            @mouseenter="onEnterBtn(index)"
            @mouseleave="onLeaveBtn()"
            @click="onClickBtn(index)">
            <div class="color-block" :class="{ blur: index !== wordColorIndex }">
              <div class="color-line" v-for="(c, index) in wc" :key="index" :style="{
                'background-color': c
              }">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { Action, Getter, namespace } from 'vuex-class'
import { BindingHelpers } from 'vuex-class/lib/bindings'
import { Events } from '../events/Events'
import { eventBus } from '../events/EventBus'
import { ICard, ICardEntry } from '../store/modules/HupuStore/State'
import CardView from './CardView.vue'

const hupuStore: BindingHelpers = namespace('Hupu')

@Component({
  components: {
    CardView
  }
})
export default class HupuView extends Vue {
  // @hupuStore.Getter public hupuCards!: ICard[]
  @hupuStore.Action private fetchData!: () => void

  private cardsReady!: Promise<void>
  private cardEntries: ICardEntry[] = []
  private cardEntriesShadow!: ICardEntry[]
  private hoveringColorBtn: number = -1
  private wordColorIndex: number = 3

  private wordColors: string[][] = [
    ['#d99cd1', '#c99cd1', '#b99cd1', '#a99cd1'],
    ['#403030', '#f97a7a'],
    ['#31a50d', '#d1b022', '#74482a'],
    ['#ffd077', '#3bc4c7', '#3a9eea', '#ff4e69', '#461e47']
  ]

  private get wordColor (): string[] {
    return this.wordColors[this.wordColorIndex]
  }

  public created (): void {
    this.cardEntriesShadow = []
    this.cardsReady = new Promise<void>((resolve: () => void): void => {
      eventBus.$on(Events.CARDS_DATA_LOADED, (hupuCards: ICard[]) => {
        this.cardEntriesShadow = hupuCards.map((c: ICard, index: number) => ({ index: index, card: c }))
        resolve()
      })
    })
    this.fetchData()
  }

  private showCards (): void {
    this.cardEntries = this.cardEntriesShadow.slice(0, 20)
  }

  private onEnterBtn (index: number): void {
    this.hoveringColorBtn = index
  }
  private onLeaveBtn (): void {
    this.hoveringColorBtn = -1
  }
  private onClickBtn (index: number): void {
    this.wordColorIndex = index
  }
}
</script>

<style lang="scss">
.nav {
  flex: 0 0 40px;
  background-color: #d84315;
}

.card-list-cont {
  flex: 1 1;
  margin-top: 10px;
  display: flex;

  .card-list::-webkit-scrollbar {
    display: none
  }

  .card-list {
    flex: 1 1;
    width: calc(100% - 50px);
    height: calc(100vh - 80px);
    overflow: scroll;
  }

  .panel {
    flex: 0 0 50px;

    .color-panel {
      margin: 5px;
      width: calc(100% - 10px);
      height: 160px;
      box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);

      .hovering {
        background-color: #ddd !important;
      }

      .selected {
        background-color: #eee !important;
      }



      .color-btn {
        transition: 'background-color' 200ms;
        width: 40px;
        height: 40px;

        .blur {
          opacity: 0.3;
        }

        .color-block {
          padding: 8px;
          width: calc(100% - 16px);
          height: calc(100% - 16px);
          display: flex;
          transition: opacity 200ms;
          .color-line {
            flex: 1 1;
          }
        }
      }
    }
  }
}
</style>
