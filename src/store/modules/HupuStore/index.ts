import { Module } from 'vuex'

import { actions } from './Actions'
import { getters } from './Getters'
import { mutations } from './Mutations'
import { IHupuStoreState, state } from './State'

import { IRootState } from '../../RootState'

// tslint:disable:variable-name
export const Hupu: Module<IHupuStoreState, IRootState> = {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
