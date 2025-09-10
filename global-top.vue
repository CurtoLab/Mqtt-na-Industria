<template>
  <header
    style="
      position: fixed;
      top: 0.5rem;
      right: 1rem;
      width: 250px;
      opacity: 1;
      pointer-events: none;
      z-index: 9999;
    "
  >
    <!-- Logo para modo claro -->
    <img 
      src="/espressif-logos/login-logo.svg" 
      alt="Espressif Logo" 
      class="block dark:hidden"
      style="width: 100%;" 
    />
    <!-- Logo para modo escuro -->
    <img 
      src="/espressif-logos/logo_title_white.svg" 
      alt="Espressif Logo" 
      class="hidden dark:block"
      style="width: 100%;" 
    />
  </header>
</template>
