import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: '数据',
    Svg: require('../../static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        世界的一切几乎都可以数据化，从而使得现代社会前所未来的产出数据与依赖数据。
      </>
    ),
  },
  {
    title: '算法',
    Svg: require('../../static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        算法渗透着我们生活的每一个层面，让我们怀疑头脑中无与伦比的想法是否只是算法在大脑皮层的映射。
      </>
    ),
  },
  {
    title: '未来',
    Svg: require('../../static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        机遇或挑战？无论如何，数据和算法将与我们相伴，携手前行是我们最优的选择。
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
