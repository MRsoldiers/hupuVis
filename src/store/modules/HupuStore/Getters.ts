import { GetterTree } from 'vuex'

import { IRootState } from '../../RootState'
import { ICard, IHupuStoreState } from './State'

export const getters: GetterTree<IHupuStoreState, IRootState> = {
  welcomeMessage: (state: IHupuStoreState): string => state.message,
  hupuCards: (state: IHupuStoreState): ICard[] => state.cards
}
