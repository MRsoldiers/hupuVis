import { MutationTree } from 'vuex'

import { MUTATIONS } from './MutationTypes'
import { ICard, IHupuStoreState } from './State'

// tslint:disable:function-name
export const mutations: MutationTree<IHupuStoreState> = {
  [MUTATIONS.SET_MESSAGE] (state: IHupuStoreState, message: string): void {
    state.message = message
  },
  [MUTATIONS.SET_CARDS] (state: IHupuStoreState, cards: ICard[]): void {
    state.cards = cards
  },
  [MUTATIONS.SET_CARDS_LOADING_PROMISE] (state: IHupuStoreState, isLoad: boolean): void {
    state.cardsLoading = isLoad
  }
}
