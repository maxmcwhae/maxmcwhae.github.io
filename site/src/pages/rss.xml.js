import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('writing');
  posts.sort((a, b) => b.data.date - a.data.date);
  return rss({
    title: 'Max McWhae — Writing',
    description: 'Technical AI safety from Perth: evaluation awareness, sandbagging, and community building.',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date,
      description: post.data.description ?? '',
      link: `/writing/${post.id}/`,
    })),
  });
}
