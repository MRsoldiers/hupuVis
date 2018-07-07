import Vue from 'vue'
import VueResource from 'vue-resource'
import { ActionContext, ActionTree } from 'vuex'

// tslint:disable-next-line:no-implicit-dependencies
import API from 'api'

import { MUTATIONS } from './MutationTypes'

import { IRootState } from '../../RootState'
import { ICard, IHupuStoreState } from './State'
import { Events } from '../../../events/Events'
import { eventBus } from '../../../events/EventBus'

const CARDS_URL: string = '/static/data/hupu-wellpost-min.json'

// tslint:disable-next-line:function-name
function CardFreeze(c: ICard, index: number): ICard {
  c.index = index

  return Object.freeze(c)
}

export const actions: ActionTree<IHupuStoreState, IRootState> = {
  async setWelcomeMessage(ctx: ActionContext<IHupuStoreState, IRootState>, message: string): Promise<void> {
    const req: API.Welcome.Request = {
      name: 'vue-webpack-ts-template'
    }
    const resp: VueResource.HttpResponse = await Vue.http.post('/api/welcome', req)
    const body: API.Welcome.Response = await (<PromiseLike<API.Welcome.Response>>resp.json())
    ctx.commit(MUTATIONS.SET_MESSAGE, body.message)
  },

  fetchData(ctx: ActionContext<IHupuStoreState, IRootState>): void {
    ctx.commit(
      MUTATIONS.SET_CARDS_LOADING_PROMISE,
      new Promise<ICard[]>(
        async (resolve: (result: ICard[]) => void): Promise<void> => {
          const cards: ICard[] = (await (<Promise<ICard[]>>(await Vue.http.get(CARDS_URL)).json())).map(CardFreeze)
          ctx.commit(MUTATIONS.SET_CARDS_LOADING_PROMISE, null)
          ctx.commit(MUTATIONS.SET_CARDS, cards)
          eventBus.$emit(Events.CARDS_DATA_LOADED, cards)
          resolve(cards)
        }
      )
    )
  }
}
