export interface IHupuStoreState {
  cards: ICard[],
  cardsLoading: boolean,
  // isCardsLoaded: boolean,
  message: string
}

export const state: IHupuStoreState = {
  cards: [],
  cardsLoading: false,
  // isCardsLoaded: false,
  message: ''
}

export interface ICard {
  author: string,
  date: string,
  hotposts: string[],
  index: number,
  link: string,
  replyNum: number,
  texeCollection: string,
  title: string,
  wellHotpost: IHotpost[],
  wordFrequency: [string, number][]
}

export interface IHotpost {
  clientAgent: string,
  nLike: number,
  postText: string,
  replier: string,
  time: string
}

export interface ICardEntry {
  index: number,
  card: ICard
}
