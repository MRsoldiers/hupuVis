import Vue from 'vue'
import { Component } from 'vue-property-decorator'

export const eventBus: Vue = new Vue()

@Component
class EventBusMixinComponent extends Vue {
  private $bus!: Vue
  public created(): void {
    this.$bus = eventBus
  }
}

Vue.mixin(EventBusMixinComponent)
