import { defineConfig } from 'vitepress'
import AutoSidebar from 'vite-plugin-vitepress-auto-sidebar';

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Mio Archives",
  description: "Mio Archives for best things",
  vite: {
    plugins: [
      // add plugin
      AutoSidebar({
        path: '',
        // You can also set options to adjust sidebar data
        // see option document below
      })
    ]
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Main', link: '/main' },
      { text: "Academics", link: '/academics' },
      { text: 'Manuals', link: '/manuals' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Purestreams' }
    ]
  }
})