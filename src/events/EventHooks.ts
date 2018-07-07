import Vue from 'vue'
// import { Events } from './Events'
// import { store } from '../store'
// import { ICard } from '../store/modules/HupuStore/State'

interface IHooks {
  [hookName: string]: ($bus: Vue) => void
}

export const hooks: IHooks = {
}
